from django.shortcuts import render,redirect
from .forms import LoanForm
from .models import Loan
# Create your views here.


def loan_index(request):
    loans = Loan.objects.filter(employee=request.user)
    # loan = Loan.objects.all()
    return render(request, 'loan/index.html', {'loans': loans})

def create_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.employee = request.user
            form.save()
            return redirect('loan')
    else:
        form = LoanForm()

    return render(request, 'loan/create.html', {'form': form})