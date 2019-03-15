from rest_framework import serializers

from restaurant.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(max_length=100)
    review = serializers.CharField(max_length=100)
    rating = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'review', 'rating']

