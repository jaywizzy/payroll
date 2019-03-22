from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Employee, AccountDetail
from .forms import EmployeeForm, AccountDetailForm

# Create your views here.

def index(request):
	employees = Employee.objects.all()

	return render(request, 'employee/index.html', {'employees': employees})

def create(request):
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('employees')
	else:
		form = EmployeeForm()

	return render(request, 'employee/create.html', {'form': form})


def detail(request, id):
	employee = Employee.objects.get(id=id)

	return render(request, 'employee/employee_detail.html', {'employee': employee})

def edit(request, id):
	employee = Employee.objects.get(id=id)
	if request.method == 'POST':
		form = EmployeeForm(request.POST or None, instance=employee)
		if form.is_valid():
			form.save()
			return redirect('employee')
	else:
		form = EmployeeForm()
	return render(request, 'employee/create.html', {'form': form, 'employee': employee})


def account_info(request, id):
	account_info = get_object_or_404(AccountDetail, id=id)
	return render(request, 'employee/account_info.html', {'account_info': account_info})


def edit_account_info(request, id):
	# employee = get_object_or_404(Employee, pk=pk)
	account_info = get_object_or_404(AccountDetail, id=id)
	form = AccountDetailForm()
	if request.method == "POST":
		form = AccountDetailForm(request.POST, instance = account_info)
		if form.is_valid():
			form.save()
		# 	return HttpResponse('YEAH')
		# else:
		# 	return HttpResponse('HELL NAH')
	else:
		form = AccountDetailForm(instance=account_info)
	return render(request, 'employee/edit_account_info.html', {'form': form})


# def edit_bank_details(request):
