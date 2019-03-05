from django.contrib import admin
from .models import Month, Year, SalaryPayroll


class YearAdmin(admin.ModelAdmin):
    list_display = ['year']
    # list_editable = ['grant_payroll']
admin.site.register(Year, YearAdmin)

class MonthAdmin(admin.ModelAdmin):
    list_display = ['month', 'year', 'month_year']

admin.site.register(Month, MonthAdmin)

class SalaryPayrollAdmin(admin.ModelAdmin):
    list_display = ['salary', 'status']

admin.site.register(SalaryPayroll, SalaryPayrollAdmin)