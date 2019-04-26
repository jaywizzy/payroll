from django.contrib import admin

from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
admin.site.register(Employee, EmployeeAdmin)

# class AccountDetailAdmin(admin.ModelAdmin):
#     list_display = ['employee', 'bank_name', 'account_number']
# admin.site.register(AccountDetail, AccountDetailAdmin)
