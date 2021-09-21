# imports db for ORM
from django.db import models as db
# imports settings to use AUTH_USER_MODEL
from django.conf import settings
#from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
#from datetime import datetime
from django.urls import reverse

class Food(db.Model):

    id = db.AutoField(primary_key=True)
    name = db.CharField(max_length=30, null=True)
    fats = db.DecimalField(max_digits=4, decimal_places=2,null=True)
    carbohydrate = db.DecimalField(max_digits=4, decimal_places=2,null=True)
    protein = db.DecimalField(max_digits=4, decimal_places=2,null=True)
    calories = db.DecimalField(max_digits=6, decimal_places=2,null=True)
    fat_ratio = db.DecimalField(max_digits=4, decimal_places=2)
    carb_ratio = db.DecimalField(max_digits=4, decimal_places=2)
    protein_ratio = db.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
      ordering = ('-name',)

    def get_absolute_url(self):
        return reverse('fooddb:list')


    def __str__(self):
        return '%s' % (self.name)