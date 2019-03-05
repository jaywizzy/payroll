from django.contrib import admin

from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']
admin.site.register(Employee, EmployeeAdmin)

class AccountDetailAdmin(admin.ModelAdmin):
    list_display = ['employee', 'bank_name', 'account_type']
admin.site.register(AccountDetail, AccountDetailAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['employee' , 'title']
admin.site.register(Department, DepartmentAdmin)

class DesignationAdmin(admin.ModelAdmin):
    list_display = ['employee', 'title', 'department']
admin.site.register(Designation, DesignationAdmin)