from django.db import models

class certifiactes_class(models.Model):
    certificates_img = models.ImageField(upload_to='all_certificates')