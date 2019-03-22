from django.shortcuts import render, redirect, get_object_or_404
from .models import Salary
from .forms import SalaryForm
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from django.template import Context, loader
from django import template
register = template.Library()
from django.http import HttpResponse
import datetime
from django.views.generic.dates import MonthArchiveView, YearArchiveView
# Create your views here.
import xlwt

class SalaryYearArchiveView(YearArchiveView):
    queryset = Salary.objects.all()
    date_field = 'date_created'
    make_object_list = True
    allow_future = True

class SalaryMonthArchiveView(MonthArchiveView):
    queryset = Salary.objects.all()
    date_field = 'date_created'
    allow_future = True

def salary_view(request):
    all_salary = Salary.objects.all()
    # query_set = Salary.objects.filter(id=id)
    context = {
        'salary': all_salary,
        # 'query_set': query_set
    }
    # salary = Salary.objects.annotate(month=ExtractMonth('date_created')).values('month').annotate(count=Count('id')).values('month', 'count')
    return render(request, 'salary/index.html', context)

def create_salary(request):

    if request.method == 'POST':
        form = SalaryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('salary')

    else:
        form = SalaryForm()

    return render(request, 'salary/create.html', {'form': form})

def edit_salary(request, id):
    salary = Salary.objects.get(id=id)
    form = SalaryForm(request.POST or None, instance = salary)
    if form.is_valid():
        form.save()
        return redirect('salary')
    else:
        form = SalaryForm()
    return render(request, 'salary/create.html', {'form': form, 'salary': salary})



# def delete_salary(request,id):

def delete_salary(request, id):
    salary = Salary.objects.get(id=id)
    if request.method == 'POST':
        salary.delete()
        return redirect('salary')
    return render(request, 'salary/index.html', {'salary': salary})


def employee_salary_report(request, id):
    employee_report = Salary.objects.filter(employee=id)

    return render(request, 'salary/employee_salary_report.html', {'employee_report': employee_report})

def export_employee_salary_xls(request, id):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="payroll.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Payroll')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Fist Name','Last Name', 'Net pay', 'Working Days', 'Gross pay', 'month', 'year']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Salary.objects.filter(employee=id).values_list('employee__first_name', 'employee__last_name','net_pay', 'total_working_days', 'gross_pay', 'date_created__month', 'date_created__year')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_salary_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="payroll.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Payroll')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Fist Name','Last Name', 'Net pay', 'Working Days', 'Gross pay', 'month', 'year']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Salary.objects.all().values_list('employee__first_name', 'employee__last_name','net_pay', 'total_working_days', 'gross_pay', 'date_created__month', 'date_created__year')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

