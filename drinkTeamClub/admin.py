from django.contrib import admin
from .models import *
# Register your models here.

class PageDrink(admin.ModelAdmin):
    readonly_fields = ('category', 'favorites')
    search_fields = ('drink_name', 'category__category_name', 'ingredients__ingredient_name')
    list_filter = ('category__category_name','ingredients__ingredient_name')
    list_display = ('drink_name', 'drink_image')
    list_display_links = ('drink_name',)
    ordering = ('id',)

class PageIngredient(admin.ModelAdmin):
    search_fields = ('ingredient_name',)

admin.site.register(Drink, PageDrink)
admin.site.register(Ingredient, PageIngredient)
admin.site.register(Category)