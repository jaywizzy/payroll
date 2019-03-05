from django.shortcuts import render
from .forms import *
from .models import *
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
    year = Year.objects.all()
    years = []
    for y in year:
        years.append(y.year)
    years.sort()
    # years = Year.objects.all()
    return render(request, 'payroll/index.html', {'years': years})

def year_details(request, id):
    year = Year.objects.get()


def login(request):

    return render(request, 'login.html')