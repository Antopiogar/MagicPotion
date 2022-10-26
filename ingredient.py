def Ingredient():
    def __init__(self, name="", fire=0, water=0, air=0, earth=0):
        self._name = name
        self._fire = fire
        self._water = water
        self._air = air
        self._earth = earth
    
    

    def str(self):
        return f"""{self._name},{self._fire},{self._water},{self._air},{self._water}"""
