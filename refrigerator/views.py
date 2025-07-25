from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .models import Ingredient
from .forms import Form
# Create your views here.
class indexview(View):
    def get(self,request):
        ingredients = Ingredient.objects.all()
        ingredients = Ingredient.objects.order_by('expiration_date')
        ingredients = Ingredient.objects.filter(quantity__gt=0)
        return render(request,'refrigerator/index.html',{'ingredients': ingredients})
index = indexview.as_view()
class addview(View):
    def get(self,request,**kwargs):
        print(kwargs)
        
        form = Form()
        if 'id' in kwargs:
            data = Ingredient.objects.get(id=kwargs['id'])
            form = Form(request.GET, instance=data)
        return render(request,
                      'refrigerator/add.html',
                      {'form': form, 'id': kwargs.get('id')})
    def post(self, request, *args, **kwargs):
        print("ADDのPost")


        print(kwargs)
        form = Form(request.POST)
        if 'id' in kwargs:
            data = Ingredient.objects.get(id=kwargs['id'])
            form = Form(request.POST, instance=data)

        # form.data['title'])

        datas = Ingredient.objects.filter(name=form.data['name'])
        for _ in datas:
            print(f'::{_}')
        
        # 入力データに誤りがないかチェック
        is_valid = form.is_valid()

        # データが正常であれば
        if is_valid:
            # モデルに登録
            form.save()
            return redirect('/')

        # データが正常じゃない
        return render(request,
                      'refrigerator/add.html',
                      {'form': form, 'id': kwargs.get('id')})
        
add = addview.as_view()     
class editview(View):   
    def get(self, request, pk):
        print(f'id:{pk},request:{request}')
        ingredient = get_object_or_404(Ingredient, pk=pk)
        form = Form(instance=ingredient)
        return render(request, 'refrigerator/edit.html', {'form': form})

    def post(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        form = Form(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'refrigerator/edit.html', {'form': form})
edit = editview.as_view()