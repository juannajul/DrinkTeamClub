from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("search_cocktail/by_name/", views.search_cocktail_by_name, name='search_by_name'),
    path("search_cocktail/by_ingredient", views.search_cocktail_by_ingredient, name='search_by_ingredient'),
    path("search_cocktail/by_category", views.search_cocktail_by_category, name='search_by_category'),
    path("your_drinks/<str:username>", views.show_user_watchlist, name='your_drinks'),
    # Api urls
    path("drink_watchlist/<int:drink_id>", views.drink_watchlist, name="drink_watchlist"),
    path("random_cocktail/", views.random_cocktail, name='random'),
]