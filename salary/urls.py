from django.urls import path
from .views import *
from django.views.generic.dates import ArchiveIndexView
from .models import Salary

urlpatterns = [
    path('', salary_view, name="salary"),
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
    path('export/xls/', export_salary_xls, name='export_salary_xls'),
    path('edit/<int:id>/', edit_salary, name="update_salary"),
    path('delete/<int:id>', delete_salary, name="delete_salary")
]
