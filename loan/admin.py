from django.contrib import admin
from .models import Loan
import datetime

# Register your models here.

class LoanAdmin(admin.ModelAdmin):
    list_display = ['employee', 'amount', 'duration', 'loan_status']
    list_editable = ['amount', 'duration', 'loan_status']

admin.site.register(Loan, LoanAdmin)


loan_duration = Loan()
loan_duration.duration = datetime.timedelta(days=30, hours=0)