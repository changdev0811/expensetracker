import datetime
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('name', max_length=100)
    address = models.CharField('address', max_length=100)
    contact_number = models.CharField('contact_number', max_length=100)

    class Meta:
        db_table = "customer"


class Category(models.Model):
    name = models.CharField('name', max_length=255)

    class Meta:
        db_table = "category"


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField('title', max_length=100)
    description = models.TextField('description')
    customer_order_no = models.IntegerField('customer_order_no', default=0)
    status = models.CharField('status', max_length=30)
    value = models.FloatField('value', default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = "project"


class Expense(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date = models.DateField("date", default=datetime.date.today)
    receipt_no = models.IntegerField('receipt_no', default=0)
    description = models.TextField('description')
    vat = models.FloatField('vat', default=0)
    total_amount = models.FloatField('total_amount', default=0)

    class Meta:
        db_table = "expense"

