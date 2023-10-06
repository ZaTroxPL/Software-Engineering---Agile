from django.urls import path
from . import views

urlpatterns = [
    path("requests", views.requests, name="requests"),
    path("requests/new", views.RequestCreate.as_view(), name="new_request"),
    path("requests/<uuid:request_id>/", views.RequestEdit.as_view(), name="requestdetail"),
    path("requests/<uuid:request_id>/approve/", views.RequestApprove.as_view(), name="requestapprove")
]