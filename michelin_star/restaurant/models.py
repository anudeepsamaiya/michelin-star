from django.db import models

# Create your models here.

class Restaurant(models.Model):
    aggregator_id = models.IntegerField(db_index=True)
    name = models.CharField(max_length=200, db_index=True, blank=True)
    rating = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    review = models.TextField(max_length=200, blank=True, null=True)
