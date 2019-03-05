from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    # path('create', add_year),
    path('login', login),

]