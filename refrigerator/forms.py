from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Ingredient, Recipe

class Form(forms.ModelForm):
    class Meta: # 構成・設定を指定できる（どのモデルと連携する、どのフィールドを使う、フォームの構成設定など）
        model = Ingredient
        fields = ('name', 'quantity', 'expiration_date') # フォームに表示するフィールドを指定
        widgets = { # 特定のフィールドの見た目を指定 datetime-localによりHTMLにて日付＋時刻入力フィールドになる
            'expiration_date': forms.DateTimeInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs): # フォームが生成されるときの初期化処理
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs = {'placeholder': '食材名'} # プレースホルダー（薄い説明文）を設定する
        self.fields["quantity"].widget.attrs = {'placeholder': '数量・グラム'}
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title','ingredients')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'レシピ名'}),
            'ingredients': forms.CheckboxSelectMultiple(),  # チェックボックスで複数選択
        }
