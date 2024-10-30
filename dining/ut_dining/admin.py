from django.contrib import admin
from .models import Food, FoodItem

admin.site.register(FoodItem)
admin.site.register(Food)