from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=20)
    contact = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=20)
    client_feedback = models.TextField()


class CustomerQuery(models.Model):
    name  = models.CharField(max_length=20)
    contact = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
