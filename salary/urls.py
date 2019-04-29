from django.urls import path
from .views import *
from django.views.generic.dates import ArchiveIndexView
from .models import Salary
# from django.contrib.auth.views import Login, Logout

urlpatterns = [
    path('', index, name="index"),
    path('payroll', salary_view, name="salary"),
    # path(''),
    path('archive/',
         ArchiveIndexView.as_view(model=Salary, date_field="date_created"),
         name="salary_archive"),
    path('<int:year>/<str:month>/',
         SalaryMonthArchiveView.as_view(),
         name="archive_month"),
    path('<int:year>/',
         SalaryYearArchiveView.as_view(),
         name="salary_year_archive"),
    path('add', create_salary, name="add_salary"),
    path('payslip/<int:id>/', payslip, name='payslip'),
    path('employee_report/<int:id>/', employee_salary_report, name="employee_report"),
    path('export/xls/', export_salary_xls, name='export_salary_xls'),
    path('export/employee/xls/<int:id>/', export_employee_salary_xls, name='export_employee_salary_xls'),
    path('edit/<int:id>/', edit_salary, name="update_salary"),
    path('delete/<int:id>', delete_salary, name="delete_salary"),
    # path('login', Login.as_view, name="login"),
    # path('logout', Lgout.as_view, name="logout"),
]
