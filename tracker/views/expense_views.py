from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tracker.models import Project, Expense, Category, Customer


@login_required
def index(request, project_id):
    expenses = Expense.objects.filter(project_id=project_id)
    return render(request, 'expense/index.html', {'expenses': expenses, 'project_id': project_id})


@login_required
def create(request, project_id):
    categories = Category.objects.all()
    return render(request, 'expense/create.html', {'categories': categories, 'project_id': project_id})


def store(request, project_id):
    date = request.POST.get('date')
    receipt_no = request.POST.get('receipt_no')
    vat = request.POST.get('vat')
    total_amount = request.POST.get('total_amount')
    category = request.POST.get('category')
    expense = Expense()
    expense.project_id = project_id
    expense.date = date
    expense.receipt_no = int(receipt_no)
    expense.vat = float(vat)
    expense.total_amount = float(total_amount)
    expense.category_id = category
    expense.save()
    return redirect('tracker:expense', project_id=project_id)


def edit(request, expense_id):
    categories = Category.objects.all()
    expense = Expense.objects.get(id=expense_id)
    project_id = expense.project_id
    return render(request, 'expense/edit.html', {'expense': expense,
                                                 'project_id': project_id,
                                                 'categories': categories})


def update(request, expense_id):
    date = request.POST.get('date')
    receipt_no = request.POST.get('receipt_no')
    vat = request.POST.get('vat')
    total_amount = request.POST.get('total_amount')
    category = request.POST.get('category')
    project_id = Expense.objects.get(id=expense_id).project_id
    Expense.objects.filter(id=expense_id).update(
                                         date=date,
                                         receipt_no=receipt_no,
                                         vat=vat,
                                         total_amount=total_amount,
                                         category=category
                                         )
    return redirect('tracker:expense', project_id=project_id)


def delete(request, expense_id):
    project_id = Expense.objects.get(id=expense_id).project_id
    Expense.objects.filter(id=expense_id).delete()
    return redirect('tracker:expense', project_id=project_id)


