from django.urls import path
from refrigerator import views as refrigerator
urlpatterns = [
    path("",refrigerator.index,name="index"),
    path("add/",refrigerator.add,name="add"),
    path('edit/<int:pk>/',refrigerator.edit,name="edit")
]
