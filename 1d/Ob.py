class Ob:
    def __init__(self , nom:str   ,surface:float):
        self._surface = surface
        self._nom:str = nom
        
    def getSurface (self):
        return self._surface
    
    def getNom (self):
        return self._nom
        
    