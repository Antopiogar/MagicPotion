class Ingredient:
    def __init__(self,id=0, name="", fire=0, water=0, air=0, earth=0):
        self._id=id
        self._name = name
        self._fire = fire
        self._water = water
        self._air = air
        self._earth = earth

    def __str__(self):
        return f"""{self._id}, {self._name}, {self._fire}, {self._water}, {self._air}, {self._earth}"""