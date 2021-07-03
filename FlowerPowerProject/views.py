from django.shortcuts import render, redirect
from models import Burger, Ingredient, BurgerIngredients
import sys


def index(request):
    burgers = Burger.objects.all()
    ingredients = Ingredient.objects.all()

    if request.method == "POST":
        if "burgerAdd" in request.POST:
            add(request)
        if "burgerDelete" in request.GET:
            delete(request)
    return render(request, "index.html", {"burgers": burgers, "ingredients": ingredients})


def add(request):
    burgerName = request.GET['burgerName']

    if 'ingredientsList' in request.GET:
        ingredientsList = request.GET.getlist('ingredientsList')
        createdBy = 1
        newBurger = Burger(title=burgerName, ingredients=ingredientsList, createdBy=createdBy)
        newBurger.save()
        for ingredientId in ingredientsList:
            ingredient = Ingredient.objects.get(id=int(ingredientId))
            burgerIngredient = BurgerIngredients(burger=newBurger, ingredient=ingredient)
            burgerIngredient.save()

    return redirect('/')  # reloading the page


def delete(request):
    checkedlist = request.GET.getlist["checkedbox"]

    for burger_id in checkedlist:
        burger = Burger.objects.get(id=int(burger_id))
        burger.delete()


def convert(a):
    it = iter(a)
    res_dct = dict(zip("ingredient", it))
    return res_dct
