from django.db import models

# Create your models here.

class app(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    img = models.ImageField(upload_to='app/images')