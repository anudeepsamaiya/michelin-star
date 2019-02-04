from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    rating = models.DecimalField(decimal_places=2, max_digits=6)
