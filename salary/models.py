from django.db import models
# from employees.models import Employee
# from core.models import User
from employees.models import *

# Create your models here.


class Salary(models.Model):
    employee = models.ForeignKey(Employee, related_name='salaries', on_delete=models.CASCADE)
    net_pay = models.IntegerField()
    total_working_days = models.IntegerField()
    travel_allowance = models.IntegerField(null=True, blank=True, default=0)
    leave_allowance = models.IntegerField(null=True, blank=True, default=0)
    performance_allowance = models.IntegerField(null=True, blank=True, default=0)
    transport_allowance = models.IntegerField(null=True, blank=True, default=0)
    medical_allowance = models.IntegerField(null=True, blank=True, default=0)
    tax_deduction = models.IntegerField(null=True, blank=True, default=0)
    other_deductions = models.IntegerField(null=True, blank=True, default=0)
    # month_pay = models.CharField(max_length=100)
    # year_salary = models.CharField(max_length=100)
    gross_pay = models.IntegerField(null=True, blank=True, default=0)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'salaries'

    # def display_month(self):
    #     month = self.date_created.strftime()

    def get_absolute_url(self):
        return reverse('salary-detail', kwargs={'pk': pk})

    def save(self, *args, **kwargs):
        # print(self.payroll)
        # self.tax_deduction = self.net_pay / 3
        print(self.tax_deduction)
        self.allowances = self.travel_allowance + self.net_pay + self.leave_allowance + self.performance_allowance + self.transport_allowance + self.medical_allowance -self.tax_deduction - self.other_deductions
        # self.payroll = self.tax_deduction - self.other_deductions
        # self.total = self.allowances - self.payroll
        self.gross_pay = self.allowances
        super(Salary, self).save(*args, **kwargs)

    def __str__(self):
        return '%s %s %s' %(self.employee, self.net_pay, self.gross_pay)



# class SalaryDeduction(models.Model):
#     employee = models.ForeignKey(User, related_name='salary payroll', on_delete=models.CASCADE)
#     total_tax_deduction = models.IntegerField()