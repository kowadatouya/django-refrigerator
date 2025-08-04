from django.urls import path
from refrigerator import views as refrigerator
urlpatterns = [
    path("",refrigerator.index,name="index"),
    path("add/",refrigerator.add,name="add"),
    path('edit/<int:pk>/',refrigerator.edit,name="edit"),
    path('offer/',refrigerator.offer,name="offer"),
    path('recipes/<int:pk>/', refrigerator.detail, name='recipe_detail'),
]
