from Ob import Ob


class Bac:
    def __init__(self, nom: str, surface: float):
        self._ob: list[Ob] = []
        self._nom: str = nom
        self._surface: float = surface

    def getObs(self):
        return self._ob

    def getNom(self):
        return self._nom

    def getSurface(self):
        return self._surface

    def getSurfaceOccupe(self):
        serface_occupe = 0
        for ob in self.getObs():
            serface_occupe += ob.getSurface()
        return serface_occupe

    def getSurfaceDispo(self):
        return self.getSurface() - self.getSurfaceOccupe()

    def addOb(self, ob: Ob):
        self._ob.append(ob)

    def __str__(self):
        resp = ""
        resp += self.getNom() + " " + str(self.getSurfaceDispo())
        # resp += "\n"
        for ob in self.getObs():
            resp += "\n " + ob.getNom() +": "+ str(ob.getSurface())
        return f"{
            resp
            }"
