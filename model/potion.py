from model.Ingredient import Ingredient

class potion():
    

    def __init__(self, name,lstIng,points=None):
        self._name = name
        self._fire = 0
        self._water = 0
        self._air = 0
        self._earth = 0
        self._ingredients = lstIng
        self._set_elements_()
        
    def _set_elements_(self):
        self._set_air()
        self._set_Fire_()
        self._set_water_()
        self._set_earth()
    
    def _set_Fire_(self):
        for i in self._ingredients:
            self._fire+=int(i._get_fire_())
            
    def _set_water_(self):
        for i in self._ingredients:
            self._water+=int(i._get_water_())
            
    def _set_air(self):
        for i in self._ingredients:
            self._air+=int(i._get_air_())
            
    def _set_earth(self):
        for i in self._ingredients:
            self._earth+=int(i._get_earth_())
              
    def _limit_1_(self):
        if self._fire>=29:
            print("controllo 1 false")
            return False
        print("controllo 1 true")
        return True
    
    def _limit_2_(self):
        if self._fire>=5:
            if self._air>=1+(self._fire)/2:
                print("controllo 2 false")
                return False
        print("Controllo 2 true")
        return True 
    
    def _limit_3_(self):
        
        if self._fire>9 and self._water<1:
            print("controllo 3 false")
            return False
        print("controllo 3 true")
        return True
        
    def _limit_4_(self):
        if self._water<self.avgAirEarth():
            print("controllo 4 false")
            return False
        print("controllo 4 true")
        return True
    
    def avgAirEarth(self):
        return (self._air+self._earth)/2
        
    
    def _can_exist(self):
        if self._limit_1_() and self._limit_2_() and self._limit_3_() and  self._limit_4_():
            return True
        return False
   
    def _points_(self):
        p=0
        pF=int(self._fire/2)
        pA=int(self._air/7)
        pW=int(self._water/5)
        pE=int(self._earth/3)
        p+=pF+pA+pW+pE
        return p

    def _restore_value_(self):
        self._fire = 0
        self._water = 0
        self._air = 0
        self._earth = 0
        
        
    def _cambia_ing(self,l):
        self._restore_value_()
        self._set_elements_()
        if self._can_exist():
            return True
        return False
        
