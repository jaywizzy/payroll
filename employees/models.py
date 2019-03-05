from django.db import models
from core.models import User
# Create your models here.

class Employee(models.Model):
    user = models.ForeignKey(User, related_name='employees', on_delete=models.CASCADE)
    # designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' %(self.user, self.designation)


class AccountDetail(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_details')
    bank_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    account_number = models.IntegerField()

    def __str__(self):
        return  '%s %s %s' %(self.employee, self.bank_name, self.account_number)


class Department(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='department')
    title = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' %(self.title, self.title)


class Designation(models.Model):
    employee = models.ForeignKey(User, related_name='designation', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='designation', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s %s' %(self.employee, self.department, self.title)
