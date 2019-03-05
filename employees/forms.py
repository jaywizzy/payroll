from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    pass

    class Meta:
        model = Employee
        fields = ('full_name', 'email', 'address')