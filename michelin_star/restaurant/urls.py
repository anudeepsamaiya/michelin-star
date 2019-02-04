from django.urls import path

from . import views


urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view()),
]
