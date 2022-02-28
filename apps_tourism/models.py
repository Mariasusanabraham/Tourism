from django.db import models

# Create your models here.
class reg(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Password = models.CharField(max_length=30)
    Confirm_Password = models.CharField(max_length=30)