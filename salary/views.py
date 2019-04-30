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
from django.contrib.auth.decorators import login_required
from django.views.generic.dates import MonthArchiveView, YearArchiveView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from employees.models import Employee


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

@login_required
def salary_view(request):
    all_salary = Salary.objects.all()
    # query_set = Salary.objects.filter(id=id)
    context = {
        'salary': all_salary,
        # 'query_set': query_set
    }
    # salary = Salary.objects.annotate(month=ExtractMonth('date_created')).values('month').annotate(count=Count('id')).values('month', 'count')
    return render(request, 'payroll/payroll_index.html', context)

@login_required
def create_salary(request):

    if request.method == 'POST':
        form = SalaryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('salary')

    else:
        form = SalaryForm()

    return render(request, 'payroll/create_payroll.html', {'form': form})

@login_required
def index(request):
    emp = Employee.objects.all()
    sal = Salary.objects.all()
    # dep_list = []
    for i in emp:
        i.deps
    a = int()
    for b in sal:
        a = b.gross_pay
        a += a
        # dep_list.append(i.department)
    # departments = set(dep_list)
    departments = len(i.deps)
    employees = len(emp)
    payroll = len(sal)
    context = {
        'departments': departments,
        'employees': employees,
        'payroll': payroll,
        'expense': a
    }
    return render(request, 'payroll/index.html', context)

@login_required
def edit_salary(request, id):
    salary = Salary.objects.get(id=id)
    form = SalaryForm(request.POST or None, instance = salary)
    if form.is_valid():
        form.save()
        return redirect('salary')
    else:
        form = SalaryForm(instance = salary)
    return render(request, 'payroll/create_payroll.html', {'form': form, 'salary': salary})


@login_required
def delete_salary(request,id):
    salary = Salary.objects.get(id=id)
    salary.delete()
    return redirect(salary_view)


# def delete_salary(request, id):
#     salary = Salary.objects.get(id=id)
#     if request.method == 'POST':
#         salary.delete()
#         return redirect('salary')
#     return render(request, 'salary/index.html', {'salary': salary})


def employee_salary_report(request, id):
    employee_report = Salary.objects.filter(employee=id)

    return render(request, 'salary/employee_salary_report.html', {'employee_report': employee_report})

def payslip(request, id):
    emp_payslip = Salary.objects.get(id=id)
    html_string = render_to_string('payroll/payslip.html', {'emp_payslip': emp_payslip})

    html = HTML(string = html_string)
    html.write_pdf(target='/tmp/payslip.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('payslip.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachement; filename="payslip.pdf"'
        return response

    return response

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
