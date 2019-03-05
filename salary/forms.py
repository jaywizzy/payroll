from django import forms
from .models import Salary


class SalaryForm(forms.ModelForm):
    pass

    class Meta:
        model = Salary
        fields = '__all__'

