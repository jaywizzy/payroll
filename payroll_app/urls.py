from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('year/<int:year>', year_month, name='year_month'),
    # path('create', add_year),
    path('login', login),

]