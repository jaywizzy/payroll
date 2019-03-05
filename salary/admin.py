from django.contrib import admin
from .models import *

# total = int(Salary.amount) + int(Salary.transport_allowance) + int(Salary.performance_allowance)


class SalaryAdmin(admin.ModelAdmin):
    list_display = ['employee', 'net_pay', 'gross_pay']


admin.site.register(Salary, SalaryAdmin)
