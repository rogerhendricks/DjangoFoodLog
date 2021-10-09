# imports db for ORM
from django.db import models as db
# imports settings to use AUTH_USER_MODEL
from django.conf import settings
#from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
#from datetime import datetime
from django.urls import reverse
from datetime import datetime
from fooddb import models as food




# class Food(db.Model):

#     meal_choices = (
#         ('Breakfast', 'Breakfast'),
#         ('Lunch', 'Lunch'),
#         ('Dinner', 'Dinner'),
#         ('Snack','Snack')
#     )

#     id = db.AutoField(primary_key=True)
#     mealDate = db.DateField(default=datetime.now)
#     meal = db.CharField(max_length=30, choices=meal_choices, null=True)
#     name = db.CharField(max_length=30, null=True)
#     serving = db.DecimalField(max_digits=2, decimal_places=1, null=True )
#     fats = db.DecimalField(max_digits=4, decimal_places=2,null=True)
#     carbohydrate = db.DecimalField(max_digits=4, decimal_places=2,null=True)
#     protein = db.DecimalField(max_digits=4, decimal_places=2,null=True)
#     calories = db.DecimalField(max_digits=6, decimal_places=2,null=True)
#     fat_ratio = db.DecimalField(max_digits=4, decimal_places=2)
#     carb_ratio = db.DecimalField(max_digits=4, decimal_places=2)
#     protein_ratio = db.DecimalField(max_digits=4, decimal_places=2)
#     client = db.ForeignKey(settings.AUTH_USER_MODEL, on_delete=db.CASCADE)
#     favorite = db.BooleanField(default=False)

#     class Meta:
#       ordering = ('-mealDate',)

#     def get_absolute_url(self):
#         return reverse('food:home', kwargs={"username": self.client.id})


#     def __str__(self):
#         return '%s %s %i' % (self.meal, self.name, self.calories)
      


class DailyFood(db.Model):

  id = db.AutoField(primary_key=True)
  client = db.ForeignKey(settings.AUTH_USER_MODEL, on_delete=db.CASCADE)
  Day = db.DateField()
  daily_calories = db.PositiveIntegerField(null=True)
  daily_fat_ratio = db.DecimalField(max_digits=4, decimal_places=2)
  daily_carb_ratio = db.DecimalField(max_digits=4, decimal_places=2)
  daily_protein_ratio = db.DecimalField(max_digits=4, decimal_places=2)

  def __str__(self):
    return "%s %i %i %i %i" % (self.Day, self.daily_calories, self.daily_fat_ratio, self.daily_carb_ratio, self.daily_protein_ratio)


class Food(db.Model):

  meal_choices = (
      ('Breakfast', 'Breakfast'),
      ('Lunch', 'Lunch'),
      ('Dinner', 'Dinner'),
      ('Snack','Snack')
    )

  id = db.AutoField(primary_key=True)
  mealDate = db.DateField(default=datetime.now)
  meal = db.CharField(max_length=30, choices=meal_choices, null=True)
  serving = db.DecimalField(max_digits=2, decimal_places=1, null=True )
  food = db.ForeignKey(food.Food, on_delete=db.DO_NOTHING, null=True, related_name ='food')
  calories = db.DecimalField(max_digits=6, decimal_places=2,null=True)
  client = db.ForeignKey(settings.AUTH_USER_MODEL, on_delete=db.CASCADE)
  

  class Meta:
      ordering = ('-mealDate',)

  def get_absolute_url(self):
        return reverse('food:home', kwargs={"pk": self.pk})

  def __str__(self):
        return '%s %s %s' % (self.mealDate, self.meal, self.food)


