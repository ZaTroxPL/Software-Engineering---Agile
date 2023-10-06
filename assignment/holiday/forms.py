from django import forms
from .models import HolidayRequest

class RequestCreateForm(forms.ModelForm):
    class Meta:
        model = HolidayRequest
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'class':'form-control datepicker','autocomplete':'off'}),
            'end_date': forms.DateInput(attrs={'class':'form-control datepicker','autocomplete':'off'})
        }

class RequestEditForm(forms.ModelForm):
    class Meta:
        model = HolidayRequest
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'class':'form-control datepicker','autocomplete':'off'}),
            'end_date': forms.DateInput(attrs={'class':'form-control datepicker','autocomplete':'off'})
        }

class RequestApproveForm(forms.ModelForm):
    class Meta:
        model = HolidayRequest
        fields = ['start_date', 'end_date', 'approved']
        widgets = {
            'start_date': forms.DateInput(attrs={'class':'form-control datepicker','autocomplete':'off','readonly':True,'reuqired':False,'disabled':True}),
            'end_date': forms.DateInput(attrs={'class':'form-control datepicker','autocomplete':'off','readonly':True,'reuqired':False,'disabled':True}),
            'approved': forms.CheckboxInput(attrs={'class':'form-control form-check-input','type':'checkbox'})
        }

    def __init__(self, *args, **kwargs):
        super(RequestApproveForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].required = False
        self.fields['end_date'].required = False
