from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=400)
    image=models.ImageField(upload_to="image/cover",null=True,blank=True)

    def __str__(self):
        return self.name
