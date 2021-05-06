from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    return render(request, "../templates/drinkTeam/index.html")

def random_cocktail(request):
    url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
    r = requests.get(url)
    r2 = r.json()
    print("---------------------------")
    #print(r.status_code)
    print("---------------------------")
    #print(r.headers)
    print("---------------------------")
    print(r)
    print("---------------------------")
    print(r.json())
    print("---------------------------")
    
    drinks = r2['drinks']
    print(drinks)
    drink_list = []
    drink_dict = {}
    for drink in drinks:
        print(drink)
        dic = drink.copy()
        for key, value in dic.items():
            if value != None:
                drink_dict[key] = value
    print("---------------------------")
    print(drink_dict)
    return render(request, "../templates/drinkTeam/index.html")
