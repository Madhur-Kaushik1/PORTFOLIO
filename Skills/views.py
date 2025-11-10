from django.shortcuts import render
from .models import database, frontend_skills, dsa, lang, framework

def skills_fun(request):
    database_var = database.objects.all()
    frontend_var = frontend_skills.objects.all()
    dsa_var = dsa.objects.all()
    lang_var = lang.objects.all()
    frame_var = framework.objects.all()

    skills_dict = {
        'database_var': database_var,
        'frontend_var': frontend_var,
        'dsa_var': dsa_var,
        'lang_var': lang_var,
        'frame_var': frame_var
    }
    return render(request, 'Skills/skills.html', skills_dict)