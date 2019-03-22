from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='employees'),
	path('create/', create, name="create_employee"),
	path('detail/<int:id>', detail, name="employee_detail"),
	path('edit/<int:id>/', edit, name="edit_employee"),
	# path('delete/<int:id>/', delete, name="delete"),

	path('account_info/<int:id>/', account_info, name="account_info"),
	path('edit_account_info/<int:id>/', edit_account_info, name="edit_account_info"),


]