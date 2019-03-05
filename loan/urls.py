from django.urls import path
from .views import *
urlpatterns = [
    path('', loan_index, name = "loan"),
    path('apply', create_loan, name='apply_loan'),
]