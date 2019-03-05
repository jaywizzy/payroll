from django.db import models
# from employees.models import Employee
from core.models import User
# from django.http import redirect
from django.contrib import messages
from salary.models import Salary
# from loan import Loan
# Create your models here.



class Year(models.Model):
    year = models.IntegerField(unique=True)

    def __str__(self):
        return '%s' %(self.year)

class Month(models.Model):
    months = (
        ('jan', 'January'), ('feb', 'February'), ('mar', 'March'),
        ('apr', 'April'), ('may', 'May'), ('jun', 'June'), ('jul', 'July'),
        ('aug', 'August'), ('sep', 'September'), ('oct', 'October'),
        ('nov', 'November'), ('dec', 'December')
    )
    month = models.CharField(max_length=100, choices=months)
    month_year = models.CharField(max_length=100, unique=True, blank=True, null=True)
    year = models.ForeignKey(Year, related_name='months', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # self.month_year = self.month + str(self.year)
        try:
            self.month_year = self.month + str(self.year)
        except IntegrityError:
            return messages.warning(request, 'month already exist in year')
        super(Month, self).save(*args, **kwargs)
    def __str__(self):
        return '%s' %(self.month)

class SalaryPayroll(models.Model):
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE, related_name='salary_payrolls')
    month = models.ForeignKey(Month, on_delete=models.CASCADE, related_name='salary_payrolls')
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(null=True)
#
#     def __str__(self):
#         return '%s %s %s' %(self.employee, self.title, self.type)

