from django.db import models

# Create your models here.

class RegUser(models.Model):
    name = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField()
