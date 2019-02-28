from django.db import models

# Create your models here.


class ModelForm(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    mpg = models.DecimalField(max_digits=5,decimal_places=1)


