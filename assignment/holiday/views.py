from datetime import date
from typing import Any
from django import http
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.views import generic
from django.db.models import Q
from .models import HolidayRequest
from .forms import RequestApproveForm, RequestCreateForm, RequestEditForm
from users.models import Employee, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def requests(request):
    holiday_requests = HolidayRequest.objects.filter(requested_by=request.user).order_by('-requested_date')

    employee = Employee.objects.get(user=request.user)
    approving_employees = Employee.objects.filter(approval_group=employee.belonging_group)
    query = Q()
    for approvingEmployee in approving_employees:
        query |= Q(requested_by=approvingEmployee.user)

    #if query is empty, make sure it isn't used
    if not query.children:
        awaiting_requests = HolidayRequest.objects.none
    else:
        query &= Q(approved=None)
        awaiting_requests = HolidayRequest.objects.filter(query).order_by('-requested_date')

    context = {
        "holiday_requests": holiday_requests,
        "awaiting_requests": awaiting_requests
    }    
    return render(request, "holidayrequest/index.html", context)

class RequestCreate(LoginRequiredMixin, generic.CreateView):
    model = HolidayRequest
    form_class = RequestCreateForm
    template_name = "holidayrequest/request_create.html"
    success_url = "/requests"
    
    def form_valid(self, form):
        form.instance.requested_by = self.request.user
        form.instance.requested_date = date.today()
        return super().form_valid(form)
    
class RequestEdit(LoginRequiredMixin, generic.UpdateView):
    model = HolidayRequest
    form_class = RequestEditForm
    template_name = "holidayrequest/request_edit.html"
    success_url = "/requests"
    pk_url_kwarg = 'request_id'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        # check if current user created this holiday request
        holreq = HolidayRequest.objects.get(id=kwargs.get('request_id'))
        if holreq.requested_by.pk != request.user.pk:
            return HttpResponseForbidden('You are not authorized to edit this holiday request.')
        
        return super().dispatch(request, *args, **kwargs)
    
class RequestApprove(LoginRequiredMixin, generic.UpdateView):
    model = HolidayRequest
    form_class = RequestApproveForm
    template_name = "holidayrequest/request_approve.html"
    success_url = "/requests"
    pk_url_kwarg = 'request_id'

    def form_valid(self, form):
        # make sure that even if user changed the html to make fields editable, the values won't change
        form.instance.start_date = HolidayRequest.objects.get(id=form.instance.id).start_date
        form.instance.end_date = HolidayRequest.objects.get(id=form.instance.id).end_date
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):        
        # check if current user belongs to the right approval group
        holreq = HolidayRequest.objects.get(id=kwargs.get('request_id'))
        holreq_employee = Employee.objects.get(user=holreq.requested_by)
        user_employee = Employee.objects.get(user=request.user)
        if (holreq_employee.approval_group != user_employee.belonging_group):
            return HttpResponseForbidden('You are not authorized to approve this holiday request.')
        
        return super().dispatch(request, *args, **kwargs)
    