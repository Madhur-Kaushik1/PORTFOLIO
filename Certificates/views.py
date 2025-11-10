from django.shortcuts import render
from .models import certifiactes_class

def certificates_fun(request):
    certificates_var = certifiactes_class.objects.all()
    return render(request, 'Certificates/certificates.html', {'certificates_var': certificates_var})