from django.db import models
from django.db.models.signals import post_save
# Create your models here.

class Employee(models.Model):
    # user = models.ForeignKey(User, related_name='employees', on_delete=models.CASCADE)
    deps = (
    ('Applications', 'Applications'), ('Network & Security','Network & Security'),
    ('Solutions', 'Solutions'),('Human Resource', 'Human Resource'),
     ('Sales', 'Sales'), ('Finance', 'Finance'), ('Infrastructure', 'Infrastructure'),
    ('Projects', 'Projects'), ('Research & Development', 'Research & Development')
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=deps)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100, null=True)
    account_number = models.IntegerField(null = True)
    account_type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)


# class AccountDetail(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='account_details')
#     bank_name = models.CharField(max_length=100, null = True)
#     account_type = models.CharField(max_length=100, null = True)
#     account_number = models.IntegerField(null = True)
#
#     def __str__(self):
#         return  '%s %s %s' %(self.employee, self.bank_name, self.account_number)
#
# def create_acct_detail(sender, **kwargs):
#     employee = kwargs["instance"]
#     if kwargs["created"]:
#         employee_account_details = AccountDetail(employee = employee)
#         employee_account_details.save()
#
# post_save.connect(create_acct_detail, sender = Employee)
