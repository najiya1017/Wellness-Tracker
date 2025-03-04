from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meal(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    name=models.CharField(max_length=100)

    MEAL_TYPES=(

        ("breakfast","breakfast"),
        ("lunch","lunch"),
        ("dinner","dinner"),
        ("snack","snack")
    )

    meal=models.CharField(max_length=100,choices=MEAL_TYPES,default="breakfast")

    calories=models.IntegerField()

    date=models.DateField(auto_now_add=True)

    def _str_(self):
        return self.name
