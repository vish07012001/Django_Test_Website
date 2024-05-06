from django.db import models

# Create your models here.
class about(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=800)

    # upload_to='about/' is the folder where the image will be stored
    image = models.ImageField(upload_to='about/') #     pip install pillow

    # This will show the title of the object in the admin panel, otherwise it will show object1, object2, etc.
    def __str__(self):
        return self.title
    
class slider(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=800)
    image = models.ImageField(upload_to='slider/')

    def __str__(self):
        return self.title
    
class client(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=400)
    image = models.ImageField(upload_to='client/')

    def __str__(self):
        return self.name