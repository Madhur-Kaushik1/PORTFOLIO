from django.db import models

class projects_class(models.Model):
    pro_name = models.CharField(max_length=20)
    web_url = models.URLField()
    code_url = models.URLField()
    pro_img = models.ImageField(upload_to='project_image')

    def __str__(self):
        return self.pro_name