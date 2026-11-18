# Create your views here.
# expenses/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Transaction
from .forms import TransactionForm

def dashboard(request):
    # Process form submission
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()

    # Query all transactions ordered by most recent
    transactions = Transaction.objects.all().order_by('-date')

    # Aggregations using Django ORM Sum
    total_income = transactions.filter(transaction_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(transaction_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
    net_balance = total_income - total_expense

    context = {
        'form': form,
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_balance': net_balance,
    }
    return render(request, 'expenses/dashboard.html', context)

def delete_transaction(request, pk):
    item = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard')
    return redirect('dashboard')