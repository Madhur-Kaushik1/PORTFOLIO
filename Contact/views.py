from django.shortcuts import render

def contact_fun(request):
    return render(request, 'Contact/contact.html')