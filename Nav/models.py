from django.db import models

class CV(models.Model):
    name = models.CharField(max_length=25)
    file = models.FileField(upload_to='my_CV')

    def __str__(self):
        return self.name