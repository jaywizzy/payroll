from django.urls import path
from django.views.generic.dates import ArchiveIndexView
# from .models import Article
from .views import *

urlpatterns = [
    path('', index),
    # path('archive/', ArchiveIndexView.as_view(model=Article, date_field="pub_date"), name="article_archive"),
    path('year/<int:year>', year_month, name='year_month'),
    path('month/<int:month>', payroll_salary, name='payroll_salary'),
    # path('create', add_year),
    path('login', login),

]
