from django.db import models



class Food(models.Model):

    name = models.CharField(max_length=100)
    extra = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FoodItem(models.Model):

    day = models.CharField(max_length=10)
    date = models.DateField()
    type = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    foods = models.ManyToManyField(Food)

    def __str__(self):
        return f"{self.day} {self.type}"