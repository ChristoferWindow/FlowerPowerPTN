from django.utils import timezone

from django.test import TestCase

from models import Burger

class BurgerModelTest(TestCase):
    def testIngredientsExceedLimit(self):
        ingredients = ['pszenna', 'pomidory', 'ogorek', 'tofu', 'cebula', 'sos czosnkowy']
        burger = Burger(title='test', ingredients=ingredients, created=timezone.now().strftime("%Y-%m-%d"), createdBy=1)
        self.assertIs(burger.isLimitExcceded(), True)

    def testIngredientsDontExceedLimit(self):
        ingredients = ['pszenna', 'pomidory', 'sos czosnkowy']
        burger = Burger(title='test', ingredients=ingredients, created=timezone.now().strftime("%Y-%m-%d"), createdBy=1)
        self.assertIs(burger.isLimitExcceded(), False)
