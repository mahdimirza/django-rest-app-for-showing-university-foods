from django.contrib import admin
from django.urls import path,include
from .views import FoodListCreateAPIView, allFoodItems, getNextFoodsAPIView, justLuanchAPIView


urlpatterns = [
    path('all-foods/', allFoodItems.as_view()),
    path('dining/', getNextFoodsAPIView.as_view()),
    path('insert-foods/', FoodListCreateAPIView.as_view()),
    path('just-luanch/', justLuanchAPIView.as_view())
]
