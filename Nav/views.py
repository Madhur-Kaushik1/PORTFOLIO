from django.shortcuts import render
from .models import CV
from django.http import FileResponse
from Skills.models import frontend_skills, database, dsa, framework, lang
from Projects.models import projects_class
from Certificates.models import certifiactes_class

def navbar(request):
    Dic = {
        'frontend_var': frontend_skills.objects.all(),
        'database_var': database.objects.all(),
        'dsa_var': dsa.objects.all(),
        'frame_var': framework.objects.all(),
        'lang_var': lang.objects.all(),
        'pro_dict': projects_class.objects.all(),
        'certificates_var': certifiactes_class.objects.all()
    }

    return render(request, 'Nav/Home.html', Dic)

def Cv_fun(request):
    cv_var = CV.objects.last()
    return FileResponse(cv_var.file.open('rb'), as_attachment=True, filename="Madhur_Kaushik_CV.pdf")