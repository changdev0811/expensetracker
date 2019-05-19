from django.urls import path
from tracker.views import auth_views
from tracker.views import landing_views
from tracker.views import customer_views
from tracker.views import project_views
from tracker.views import expense_views


app_name = 'tracker'
urlpatterns = [
    # auth
    path('login/', auth_views.login_view, name='login'),
    path('logout', auth_views.logout_view, name='logout'),

    # landing
    path('', landing_views.index, name='index'),

    # customer
    path('customer', customer_views.index, name='customer'),
    path('customer/create', customer_views.create, name='customer_create'),
    path('customer/store', customer_views.store, name='customer_store'),
    path('customer/<int:id>', customer_views.edit, name='customer_edit'),
    path('customer/<int:id>/update', customer_views.update, name='customer_update'),
    path('customer/<int:id>/delete', customer_views.delete, name='customer_delete'),

    # project
    path('project', project_views.index, name='project'),
    path('project/create', project_views.create, name='project_create'),
    path('project/store', project_views.store, name='project_store'),
    path('project/<int:id>', project_views.edit, name='project_edit'),
    path('project/<int:id>/update', project_views.update, name='project_update'),
    path('project/<int:id>/delete', project_views.delete, name='project_delete'),

    # expense
    path('project/<int:project_id>/expense', expense_views.index, name='expense'),
    path('project/<int:project_id>/expense/create', expense_views.create, name='expense_create'),
    path('project/<int:project_id>/expense/store', expense_views.store, name='expense_store'),
    path('expense/<int:expense_id>', expense_views.edit, name='expense_edit'),
    path('expense/<int:expense_id>/update', expense_views.update, name='expense_update'),
    path('expense/<int:expense_id>/delete', expense_views.delete, name='expense_delete'),

]