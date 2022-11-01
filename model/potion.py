import math
from model.Ingredient import Ingredient


class potion():
    

    def __init__(self, name):
        self._name = name
        self._fire = 0
        self._water = 0
        self._air = 0
        self._earth = 0
        self_ingredients = []

    def _add_ingredient(self, ingredient):
        a = Ingredient()
        if self.canAddIngredient():
            self._ingredients.append(ingredient)
            return True
        else:
            return False

    def canAddIngredient(self, ingredient):
        canMade = True
        if (self._fire+ingredient._fire) > 29:
            canMade = False
        if (self._air+ingredient._air) > (int((self._fire+ingredient._fire)/2)+1) and (int((self._fire+ingredient._fire)/2)+1) >= 5:
            canMade = False
        if (self._fire+ingredient._fire) > 9:
            if(self._water+ingredient._water) < 1:
                return False
        if (self._water+ingredient._water) > math.avg(((self._air+ingredient._air), (self._earth+ingredient._earth))):
            canMade=False
        return canMade

    def _point_(self):
        point = int(self._fire)+int(self._water) + \
            int(self._air)+int(self._earth)
        return point
