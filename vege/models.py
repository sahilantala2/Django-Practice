from django.db import models


# Create your models here.
class Receipe(models.Model):
    recepie_name = models.CharField(max_length=100)
    recepie_description = models.TextField()
    recepie_image = models.ImageField(upload_to="recepie_img")