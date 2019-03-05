from django import forms
from .models import Loan
from employees.models import Employee


class LoanForm(forms.ModelForm):
    pass

    class Meta:
        model = Loan
        fields = ('amount',)