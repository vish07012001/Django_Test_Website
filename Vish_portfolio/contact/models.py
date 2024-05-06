from django.db import models

# Create your models here.
class contactlist(models.Model):
    address = models.TextField(max_length=800)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class contactform(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    messgae = models.TextField(max_length=800)

    def __str__(self):
        return self.email