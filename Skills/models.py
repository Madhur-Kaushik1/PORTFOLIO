from django.db import models

class frontend_skills(models.Model):
    image = models.ImageField(upload_to='skills_img')
    frontend_name = models.CharField(max_length=20)

    def __str__(self):
        return self.frontend_name
    
class lang(models.Model):
    image = models.ImageField(upload_to='skills_img')
    lang = models.CharField(max_length=20)

    def __str__(self):
        return self.lang
    
class framework(models.Model):
    image = models.ImageField(upload_to='skills_img')
    framework = models.CharField(max_length=20)

    def __str__(self):
        return self.framework
    
class database(models.Model):
    image = models.ImageField(upload_to='skills_img')
    database = models.CharField(max_length=20)

    def __str__(self):
        return self.database
    
class dsa(models.Model):
    image = models.ImageField(upload_to='skills_img')
    dsa = models.CharField(max_length=20)

    def __str__(self):
        return self.dsa