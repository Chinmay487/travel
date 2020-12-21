from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField(max_length=4)
    image = models.ImageField(upload_to='dest_img')