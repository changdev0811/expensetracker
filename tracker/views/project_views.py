from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tracker.models import Project, Expense, Category, Customer


@login_required
def index(request):
    user_id = request.user.id
    projects = Project.objects.filter(user_id=user_id)
    return render(request, 'project/index.html', {'projects': projects})


@login_required
def create(request):
    categories = Category.objects.all()
    user_id = request.user.id
    customers = Customer.objects.filter(user_id=user_id)
    return render(request, 'project/create.html', {'categories': categories, 'customers': customers})


def store(request):
    # project
    user_id = request.user.id
    title = request.POST.get('title')
    description = request.POST.get('description')
    customer_id = request.POST.get('customer_id')
    customer_order_no = request.POST.get('customer_order_no')
    status = request.POST.get('status')
    amount = request.POST.get('amount')
    project = Project()
    project.user_id = user_id
    project.customer_id = customer_id
    project.title = title
    project.description = description
    project.customer_order_no = customer_order_no
    project.status = status
    project.value = float(amount)
    project.save()
    return redirect('tracker:project')


def edit(request, id):
    categories = Category.objects.all()
    project = Project.objects.get(id=id)
    user_id = request.user.id
    customers = Customer.objects.filter(user_id=user_id)
    return render(request, 'project/edit.html', {'project': project,
                                                 'customers': customers,
                                                 'categories': categories})


def update(request, id):
    title = request.POST.get('title')
    description = request.POST.get('description')
    customer_id = request.POST.get('customer_id')
    customer_order_no = request.POST.get('customer_order_no')
    status = request.POST.get('status')
    amount = request.POST.get('amount')

    Project.objects.filter(id=id).update(title=title,
                                         description=description,
                                         customer_id=customer_id,
                                         customer_order_no=customer_order_no,
                                         status=status,
                                         value=amount
                                         )

    return redirect('tracker:project')


def delete(request, id):
    Project.objects.filter(id=id).delete()
    return redirect('tracker:project')


