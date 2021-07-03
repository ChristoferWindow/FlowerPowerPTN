from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone

class Categories(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, max_length=50, on_delete=models.PROTECT)
    class Meta:
        verbose_name = ("Ingredient")
        verbose_name_plural = ("Ingredients")
    def __str__(self):
        return self.name

class Burger(models.Model):
    ingredientsLimit = 4
    title = models.CharField(max_length=250)
    ingredients = ArrayField(models.CharField(max_length=64, blank=False),size=12,)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    createdBy = models.IntegerField(default=1)
    class Meta:
        ordering = ["-title"]
    def __str__(self):
        return self.title

    def isLimitExcceded(self):
        return self.ingredients.__len__() > self.ingredientsLimit

class BurgerIngredients(models.Model):
    burger = models.ForeignKey(Burger, max_length=50, on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredient, max_length=50, on_delete=models.PROTECT)