from rest_framework import serializers
from .models import Food, FoodItem
import jdatetime


months_shamsi = [
    "فروردین",
    "اردیبهشت",
    "خرداد",
    "تیر",
    "مرداد",
    "شهریور",
    "مهر",
    "آبان",
    "آذر",
    "دی",
    "بهمن",
    "اسفند"
]



class FoodSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ('name', 'extra', )

class FoodItemSerilizer(serializers.ModelSerializer):

    foods = FoodSerilizer(many=True)
    date = serializers.CharField(write_only=True)
    day = serializers.CharField(write_only=True)
    title = serializers.SerializerMethodField()
    class Meta:
        model = FoodItem
        fields = ('day', 'date', 'type', 'location', 'foods', 'title', )

    def get_title(self, obj):
        jalali_date = jdatetime.datetime.now().date()
        return f"{obj.type} ( { obj.day } )"
    
    def to_representation(self, instance):
        return super().to_representation(instance)

    def create(self, validated_data):
        foods_data = validated_data.pop('foods')
        date_shamsi_str = validated_data.pop('date', None)
        if date_shamsi_str:
            persian_date = jdatetime.datetime.strptime(date_shamsi_str, "%Y/%m/%d")
            gregorian_date = persian_date.togregorian()
            validated_data['date'] = gregorian_date.date()

        FoodItem_instace = FoodItem.objects.create(**validated_data)

        food_instances = [Food(**food_data) for food_data in foods_data]
        Food.objects.bulk_create(food_instances)

        FoodItem_instace.foods.set(food_instances)

        return FoodItem_instace