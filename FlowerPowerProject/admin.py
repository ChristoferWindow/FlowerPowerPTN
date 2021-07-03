from django.contrib import admin

# Register your models here.
from . import models
class BurgersAdmin(admin.ModelAdmin):
    list_display = ("title",  "ingredients", "createdBy")
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name","category")
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(models.Burger, BurgersAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.Categories, CategoriesAdmin)