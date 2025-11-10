from django.shortcuts import render
from .models import projects_class

def pro_fun(request):
    pro_dict = projects_class.objects.all()
    return render(request, 'Projects/projects.html', {'pro_dict': pro_dict})