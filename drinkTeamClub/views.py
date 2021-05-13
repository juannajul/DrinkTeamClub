import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
import requests
import random
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# For Making queries
from django.db.models import Q
from functools import reduce
from operator import or_

# Import models
from .models import Ingredient, Category, Drink
from users.models import User

# Import forms
from .forms import FormIngredientDrink, FormNameDrink, FormCategoryDrink

# Create your views here.

def index(request):
    return render(request, "../templates/drinkTeam/index.html",{
        "ingredientForm": FormIngredientDrink(),
        "drinkForm": FormNameDrink(),
        "categoryForm": FormCategoryDrink(),
    })

def random_cocktail(request):
    # Get random drink id
    drinks = Drink.objects.all()
    drinks_list = []
    [drinks_list.append(int(drink.id)) for drink in drinks]
    drinks_list_len = len(drinks_list)
    random_number_drink = random.randrange(0, drinks_list_len - 1)
    random_id_drink = drinks_list[random_number_drink]
    # Get random drink
    random_drink = Drink.objects.get(pk=random_id_drink)
    if request.method == "GET":
        return JsonResponse(random_drink.serialize())
    else:
        return JsonResponse({
            "error": "GET or PUT request required or there aren't drinks."
        }, status=400)

def search_cocktail_by_ingredient(request):
    if request.method == "POST":
        ingredient_form = FormIngredientDrink(request.POST)
        if ingredient_form.is_valid():
            ingredient = ingredient_form.cleaned_data['ingredient']
            ingredient_list = ingredient.capitalize().split()
            # Search ingredients in db
            q_object = reduce(or_, (Q(ingredient_name__icontains=ingredient) for ingredient in ingredient_list))
            print(q_object)
            try:
                ingredients = Ingredient.objects.filter(q_object)
            except Ingredient.DoesNotExist:
                return JsonResponse({
                    "error": "Ingredient doesn't exist."
                }, status=400)
            drinks_list = []
            # get drinks for each ingredient
            for ingredient in ingredients:
                drinks = Drink.objects.filter(ingredients=ingredient.id)
                for drink in drinks:
                    drinks_list.append(drink)
            
            if len(drinks_list) > 1:
                return render(request, "../templates/drinkTeam/cocktails_search.html",{
                    "drinks": drinks_list,
                })
            else:
                return JsonResponse({
                    "error": "Ingredient doesn't exist."
                }, status=400)

def search_cocktail_by_category(request):
    if request.method == 'POST':
        category_form = FormCategoryDrink(request.POST)
        if category_form.is_valid():
            category = category_form.cleaned_data['category']
            print(category)
            # get categories
            try:
                categories = Category.objects.filter(pk=category)
            except Category.DoesNotExist:
                return JsonResponse({
                    "error:" "Category doesn't exist."
                })
            drinks_list = []
            # Get drink for each category
            for category in categories:
                drinks = Drink.objects.filter(category=category.id)
                for drink in drinks:
                    drinks_list.append(drink)
            if len(drinks_list) > 1:
                return render(request, "../templates/drinkTeam/cocktails_search.html",{
                    "drinks": drinks_list,
                })
            else:
                return JsonResponse({
                    "error": "category doesn't exist."
                }, status=400)

def search_cocktail_by_name(request):
    if request.method == "POST":
        drink_form = FormNameDrink(request.POST)
        if drink_form.is_valid():
            cocktail = drink_form.cleaned_data['name_drink']
            # Get the drinks from thecocktaildb api
            url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail}'
            try:
                r = requests.get(url).json()
            except ValueError:
                return JsonResponse({
                    "error": "Write valid data"
                }, status=400)
            drinks = r['drinks']
            if drinks == None:
                return JsonResponse({
                    "error": "The drink doesn't exists."
                }, status=400)
            
            drink_list = []
            # Create drink
            for drink in drinks:
                drink_exists = Drink.objects.filter(drink_name=drink['strDrink']).exists()
                if drink_exists == False:
                    # Create ingredient
                    ingredients = [drink['strIngredient1'],drink['strIngredient2'],drink['strIngredient3'],drink['strIngredient4'],
                    drink['strIngredient5'],drink['strIngredient6'],drink['strIngredient7'],drink['strIngredient8'],drink['strIngredient9'],
                    drink['strIngredient10'],drink['strIngredient11'],drink['strIngredient12'],drink['strIngredient13'],
                    drink['strIngredient14'],drink['strIngredient15']]
                    for ingredient in ingredients:
                        if ingredient != None and Ingredient.objects.filter(ingredient_name=ingredient).exists() == False:
                            add_ingredient = Ingredient(ingredient_name=ingredient)
                            add_ingredient.save()
                    
                    # Create category
                    drink_category = drink['strCategory']
                    if drink_category != None and Category.objects.filter(category_name=drink_category).exists() == False:
                        add_category = Category(category_name=drink_category)
                        add_category.save()
                    
                    # Create drink
                    drink_name = drink['strDrink']
                    drink_instruction = drink['strInstructions']
                    drink_image = drink['strDrinkThumb']
                    print(drink_name)
                    print(drink_category)
                    category_instance = Category.objects.get(category_name=drink_category)
                    add_drink = Drink(
                        drink_name=drink_name,
                        drink_instructions=drink_instruction,
                        drink_image=drink_image,
                        category=category_instance
                        )
                    add_drink.save()
                    get_drink = Drink.objects.get(drink_name=drink_name)
                    for ingredient in ingredients:
                        if ingredient != None:
                            print("/")
                            print(ingredient)
                            ingredient_instance = Ingredient.objects.get(ingredient_name=ingredient)
                            get_drink.ingredients.add(ingredient_instance)
                            get_drink.save()

                    # Drink for view
                    get_drink_for_list = Drink.objects.get(drink_name=drink_name)
                    drink_list.append(get_drink_for_list)
                else:
                    # Drinks already in bd
                    drink_name = drink['strDrink']
                    get_drink_for_list = Drink.objects.get(drink_name=drink_name)
                    drink_list.append(get_drink_for_list)
            print(drink_list)
            return render(request, "../templates/drinkTeam/cocktails_search.html",{
                "drinks": drink_list
            })
    return JsonResponse({
                    "error": "Write valid data"
                }, status=400)

@login_required(login_url='login')
@csrf_exempt
def drink_watchlist(request, drink_id):
    try:
        drink = Drink.objects.get(pk=drink_id)
    except Drink.DoesNotExist:
        return JsonResponse({
            "error": "Drink not found."
        }, status=404)
    # drink watchlist
    if request.method == "PUT":
        data_drink = json.loads(request.body)
        if data_drink.get("favorites") is not None:
            print(data_drink.get("favorites"))
            if data_drink.get("favorites"):
                print("entro 0")
                if request.user in drink.favorites.all():
                    print("entro1")
                    drink.favorites.remove(request.user)
                else:
                    drink.favorites.add(request.user)
                    print("entro2")
        drink.save()
        return HttpResponse(status=204)
    elif request.method == "GET":
        return JsonResponse(drink.serialize())
    else:
        return JsonResponse({
            "error": "PUT request required"
        }, status=404)

@login_required(login_url='login')
def show_user_watchlist(request, username):
    drinks = Drink.objects.filter(favorites=request.user.id)
    return render(request, "../templates/drinkTeam/cocktails_search.html",{
                    "drinks": drinks,
                })
