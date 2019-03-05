from django.urls import path
from .views import *

urlpatterns = [
    path('', salary, name="salary"),
    path('add', create_salary, name="add_salary"),
    path('edit/<int:id>/', edit_salary, name="update_salary"),
    path('delete/<int:id>', delete_salary, name="delete_salary")
]
