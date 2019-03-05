from django.shortcuts import render, redirect
from .models import Salary
from .forms import SalaryForm
from django.db.models.functions import ExtractMonth
from django.db.models import Count

# Create your views here.

def salary(request):

    salary = Salary.objects.all()
    # salary = Salary.objects.annotate(month=ExtractMonth('date_created')).values('month').annotate(count=Count('id')).values('month', 'count')
    return render(request, 'salary/index.html', {'salary': salary})

def create_salary(request):

    if request.method == 'POST':
        form = SalaryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('salary')

    else:
        form = SalaryForm()

    return render(request, 'salary/create.html', {'form': form})

def edit_salary(request, id):
    salary = Salary.objects.get(id=id)
    form = SalaryForm(request.POST or None, instance = salary)
    if form.is_valid():
        form.save()
        return redirect('salary')

    return render(request, 'salary/create.html', {'form': form, 'salary': salary})



# def delete_salary(request,id):

def delete_salary(request, id):
    salary = Salary.objects.get(id=id)
    if request.method == 'POST':
        salary.delete()
        return redirect('salary')
    return render(request, 'salary/index.html', {'salary': salary})


