class potionLite():
    def __init__(self,id,name,points):
        self.id=id
        self.name=name
        self.points=points
        
    def __str__(self):
        return f"""{self.id}, {self.name}, {self.points}"""