class user():
    def __init__(self,id,name,passW):
        self._id=id
        self._name=name
        self._pass=passW
    
    def _is_logged(self,u,p):
        if self._name.lower()==u.lower() and self._pass==p:
            return True
        else:
            return False
    
    def __str__(self):
        return f"""{self._id}, {self._name}, {self._pass}"""