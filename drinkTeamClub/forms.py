from django import forms
from django.core import validators
from .models import Ingredient, Category, Drink

class FormIngredientDrink(forms.Form):
    ingredient = forms.CharField(label="" ,max_length=60, min_length=2, required=True,
        widget= forms.TextInput(attrs={'placeholder': 'Ingredient', 'autocomplete':'off'})
    ) 

    def clean_ingredient(self):
        # ingredient lowercase
        ingredient = self.cleaned_data['ingredient'].lower()
        return ingredient

class FormCategoryDrink(forms.Form):

    categories = Category.objects.all()
    options = []
    id_options = []
    name_options = []
    for cat in categories:
        id_category = cat.id
        name_category = cat.category_name
        option = [(cat.id, cat.category_name)]
        id_options.append(id_category)     
        name_options.append(name_category)  
        options.append(
            (id_category, name_category)
        )

    category = forms.TypedChoiceField(label="", choices=options, coerce=int)
        
class FormNameDrink(forms.Form):
    name_drink = forms.CharField(label="" ,max_length=60, min_length=2, required=True,
        widget= forms.TextInput(attrs={'placeholder': 'Cocktail name', 'autocomplete':'off'})
    ) 

    def clean_drink(self):
        # drink lowercase
        name_drink = self.cleaned_data['name_drink'].lower()
        return name_drink