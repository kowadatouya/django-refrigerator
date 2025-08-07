from django.urls import path
from refrigerator import views as refrigerator
from refrigerator import views
urlpatterns = [
    path("",refrigerator.index,name="index"),
    path("add/",refrigerator.add,name="add"),
    path('edit/<int:pk>/',refrigerator.edit,name="edit"),
    path('offer/',refrigerator.offer,name="offer"),
    path('recipes/<int:pk>/', views.detailview, name='recipe_detail'),
    path('o_edit/<int:pk>/',refrigerator.o_edit, name='offer_edit'),
    path('delete/<int:id>/', refrigerator.DeleteView, name='delete'),
]
