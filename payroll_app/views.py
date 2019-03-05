from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.urls import reverse
# Create your views here.

def add_year(request):
    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            form.save()

        m_form = MonthForm(request.POST)
        if form.is_valid():
            m_form.save()
    else:
        form = YearForm()
        m_form = MonthForm()
    return render(request, 'payroll/create.html', {'form': form, 'm_form': m_form})

def index(request):
    # year = Year.objects.all()
    # years = []
    # for y in year:
    #     years.append(y.year)
    # years.sort()
    years = Year.objects.all().order_by('year')
    return render(request, 'payroll/index.html', {'years': years})

#this function gets the year id from the index.html view <a> tag and displays the months under it
def year_month(request, year):
    # month = get_object_or_404(Month, year=year)
    months = Month.objects.filter(year=year)
    return render(request, 'payroll/year_month.html', {'months': months})

# def payroll_salary(request, month):



def login(request):

    return render(request, 'login.html')