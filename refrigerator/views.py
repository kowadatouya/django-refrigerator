from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .models import Ingredient,Recipe
from .forms import Form,RecipeForm
from django.views.decorators.csrf import csrf_protect
# Create your views here.
class indexview(View):
    def get(self,request):
        ingredients = Ingredient.objects.all()
        ingredients = Ingredient.objects.order_by('expiration_date')
        ingredients = Ingredient.objects.filter(quantity__gt=0)
        recipes = Recipe.objects.all()
        return render(request,'refrigerator/index.html',{'ingredients': ingredients,'recipes': recipes})
    # @csrf_protect
    # def update_quantities(request):
    #     if request.method == 'POST':
    #         for key, value in request.POST.items():
    #             if key.startswith('quantity_'):
    #                 try:
    #                     pk = int(key.replace('quantity_', ''))
    #                     quantity = int(value)
    #                     ingredient = Ingredient.objects.get(pk=pk)
    #                     if quantity > 0:
    #                         ingredient.quantity = quantity
    #                         ingredient.save()
    #                     else:
    #                         ingredient.delete()
    #                 except (Ingredient.DoesNotExist, ValueError):
    #                     pass
    #     return redirect('index')
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
class offerview(View):
    def get(self,request,**kwargs):
        print(kwargs)
        
        form = RecipeForm()
        if 'id' in kwargs:
            data = Recipe.objects.get(id=kwargs['id'])
            form = RecipeForm(request.GET, instance=data)
        return render(request,
                      'refrigerator/offer.html',
                      {'form': form, 'id': kwargs.get('id')})
    def post(self, request, *args, **kwargs):
        print("offerのPost")


        print(kwargs)
        form = RecipeForm(request.POST)
        if 'id' in kwargs:
            data = Recipe.objects.get(id=kwargs['id'])
            form = RecipeForm(request.POST, instance=data)

        # form.data['title'])

        datas = Recipe.objects.filter(title=form.data['title'])
        for _ in datas:
            print(f'::{_}')
        
        # 入力データに誤りがないかチェック
        if request.method == 'POST':
            form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()  # ← 先に保存！

            # 未登録食材の追加処理
            extra_ingredients = request.POST.getlist('extra_ingredients')
            for name in extra_ingredients:
                name = name.strip()
                if name:
                    # 存在しない食材を作成（既にあれば取得）
                    ingredient, created = Ingredient.objects.get_or_create(
                        name=name,
                        defaults={'quantity': 0, 'expiration_date': '2099-12-31'}
                    )
                    recipe.ingredients.add(ingredient)  # ← この時点で recipe は保存済み

            return redirect('offer')
        else:
            form = RecipeForm()
offer = offerview.as_view()