from django import forms
from .models import Employee, AccountDetail

class EmployeeForm(forms.ModelForm):
    pass

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'department', 'designation', 'phone_number')

class AccountDetailForm(forms.ModelForm):

	class Meta:
		model = AccountDetail
		fields = ('bank_name', 'account_number', 'account_type')