from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tracker.models import Customer


@login_required
def index(request):
    user_id = request.user.id
    customers = Customer.objects.filter(user_id=user_id)
    return render(request, 'customer/index.html', {'customers': customers})


@login_required
def create(request):
    return render(request, 'customer/create.html')


def store(request):
    user_id = request.user.id
    name = request.POST.get('name')
    address = request.POST.get('address')
    contact_number = request.POST.get('contact_number')
    customer = Customer()
    customer.user_id = user_id
    customer.name = name
    customer.address = address
    customer.contact_number = contact_number
    customer.save()
    return redirect('tracker:customer')


def edit(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'customer/edit.html', {'customer': customer})


def update(request, id):
    name = request.POST.get('name')
    address = request.POST.get('address')
    contact_number = request.POST.get('contact_number')
    Customer.objects.filter(id=id).update(name=name,
                                          address=address,
                                          contact_number=contact_number)
    return redirect('tracker:customer')


def delete(request, id):
    Customer.objects.filter(id=id).delete()
    return redirect('tracker:customer')


