from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Employee #, AccountDetail
from .forms import EmployeeForm #, AccountDetailForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
	employees = Employee.objects.all()
	return render(request, 'payroll/employees_index.html', {'employees': employees})

@login_required
def create(request):
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('employees')
	else:
		form = EmployeeForm()
	return render(request, 'payroll/create_employee.html', {'form': form})


@login_required
def detail(request, id):
	employee = Employee.objects.get(id=id)
	return render(request, 'payroll/employee_index.html', {'employee': employee})

@login_required
def edit(request, id):
	employee = Employee.objects.get(id=id)
	if request.method == 'POST':
		form = EmployeeForm(request.POST or None, instance=employee)
		if form.is_valid():
			form.save()
			# return redirect('employee_detail' )
			return detail(request, id)
	else:
		form = EmployeeForm(instance=employee)
	return render(request, 'payroll/create_employee.html', {'form': form, 'employee': employee})

@login_required
def delete_employee(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect(index)

# def account_info(request, id):
# 	account_info = get_object_or_404(AccountDetail, id=id)
# 	return render(request, 'employee/account_info.html', {'account_info': account_info})
#
#
# def edit_account_info(request, id):
# 	# employee = get_object_or_404(Employee, pk=pk)
# 	account_info = get_object_or_404(AccountDetail, id=id)
# 	form = AccountDetailForm()
# 	if request.method == "POST":
# 		form = AccountDetailForm(request.POST, instance = account_info)
# 		if form.is_valid():
# 			form.save()
# 		# 	return HttpResponse('YEAH')
# 		# else:
# 		# 	return HttpResponse('HELL NAH')
# 	else:
# 		form = AccountDetailForm(instance=account_info)
# 	return render(request, 'employee/edit_account_info.html', {'form': form})


# def edit_bank_details(request):
