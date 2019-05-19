from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker.models import Project


@login_required
def index(request):
    user_id = request.user.id
    projects = Project.objects.filter(user_id=user_id).order_by('-created_at')[:5]
    return render(request, 'landing_page.html', {'projects': projects, 'user_id': user_id})
