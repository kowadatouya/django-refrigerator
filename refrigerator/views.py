from django.shortcuts import render
from django.views import View
from .models import Ingredient
from .forms import Form
# Create your views here.
class indexview(View):
    def get(self,request):
        ingredients = Ingredient.objects.all()
        return render(request,'refrigerator/index.html',{'ingredients': ingredients})
index = indexview.as_view()
class addview(View):
    def get(self,request,**kwargs):
        print(kwargs)
        
        form = Form()
        if 'id' in kwargs:
            data = Ingredient
        
add = addview.as_view()        