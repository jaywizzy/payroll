from django.db import models
# from employees.models import Employee
from core.models import User
import datetime

# Create your models here.

class Loan(models.Model):
    employee = models.ForeignKey(User, related_name='loans', on_delete=models.CASCADE)
    amount = models.IntegerField()
    duration = models.DurationField(default=datetime.timedelta(days=30, hours=12))
    loan_status = models.BooleanField(null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  '%s %s %s' %(self.employee, self.amount, self.loan_status)


loan_duration = Loan()
loan_duration.duration = datetime.timedelta(days=30, hours=0)