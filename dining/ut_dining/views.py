from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Food, FoodItem
from .serilizers import FoodItemSerilizer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from datetime import datetime
import jdatetime


class FoodListCreateAPIView(ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerilizer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class allFoodItems(APIView):
    serilizer_class = FoodItemSerilizer
    def get(self, request, *args, **kwargs):
        q = FoodItem.objects.all()
        serilizer = FoodItemSerilizer(q, many=True)
        return Response(data=serilizer.data, status=status.HTTP_200_OK)
    

class getNextFoodsAPIView(APIView):
    serilizer_class = FoodItemSerilizer
    def get(self, request, *args, **kwargs):
        now = datetime.now().date()
        qset = FoodItem.objects.all().order_by('date')
        if(datetime.now().hour <= 15):
            data = qset.filter(date__gte=now)[:2]
            serilizer = FoodItemSerilizer(data, many=True)
            return Response(data=serilizer.data, status=status.HTTP_200_OK)
        else:
            data = qset.filter(date__gte=now)
            if(data[0].type == "ناهار"):
                serilizer = FoodItemSerilizer(data[1:3], many=True)
            else:
                serilizer = FoodItemSerilizer(data[:2], many=True)
            return Response(data=serilizer.data, status=status.HTTP_200_OK)
        
class justLuanchAPIView(APIView):
    serilizer_class = FoodItemSerilizer
    def get(self, request, *args, **kwargs):
        now = datetime.now().date()
        qset = FoodItem.objects.filter(type='ناهار').order_by('date')
        if(datetime.now().hour <= 15):
            data = qset.filter(date__gte=now)[:2]
            serilizer = FoodItemSerilizer(data, many=True)
            return Response(data=serilizer.data, status=status.HTTP_200_OK)
        else:
            data = qset.filter(date__gte=now)
            serilizer = FoodItemSerilizer(data[1:3], many=True)
            return Response(data=serilizer.data, status=status.HTTP_200_OK)