from Bac import Bac
from Ob import Ob

def ff1D (obs:list[Ob] , first_bac:Bac):
    bacs:list[Bac] = []
    surface_prevue:float = 0
    bacs.append(first_bac)
    for ob in obs:
        surface_prevue= ob.getSurface()
        bac_cible:Bac = None
        for bac in bacs:
            if (bac.getSurfaceDispo() >= surface_prevue):
                bac_cible = bac
                break
        if not bac_cible:
            index:int = len(bacs)+1
            new_nom = "B" +str(index)
            new_bac = Bac(new_nom , first_bac.getSurface())
            if new_bac.getSurfaceDispo() >= surface_prevue:
                new_bac.addOb(ob)
                bacs.append(new_bac)
        else:
            bac_cible.addOb(ob)
    return bacs  


def bf1D (obs:list[Ob] , first_bac:Bac):
    bacs:list[Bac] = []
    surface_prevue:float = 0
    bacs.append(first_bac)
    for ob in obs:
        surface_prevue= ob.getSurface()
        bac_cible:Bac = bacs[0]
        for bac in bacs:
            if (bac.getSurfaceDispo() >= surface_prevue and bac.getSurfaceDispo() < bac_cible.getSurfaceDispo() ):
                bac_cible = bac
        if  bac_cible.getSurfaceDispo() < surface_prevue:
            bac_cible = None
        if not bac_cible:
            index:int = len(bacs)+1
            new_nom = "B" +str(index)
            new_bac = Bac(new_nom , first_bac.getSurface())
            if new_bac.getSurfaceDispo() >= surface_prevue:
                new_bac.addOb(ob)
                bacs.append(new_bac)
        else:
            bac_cible.addOb(ob)
    return bacs  


def wf1D (obs:list[Ob] , first_bac:Bac):
    bacs:list[Bac] = []
    surface_prevue:float = 0
    bacs.append(first_bac)
    for ob in obs:
        surface_prevue= ob.getSurface()
        bac_cible:Bac = bacs[0]
        for bac in bacs:
            if (bac.getSurfaceDispo() >= surface_prevue and bac.getSurfaceDispo() > bac_cible.getSurfaceDispo() ):
                bac_cible = bac
        if  bac_cible.getSurfaceDispo() < surface_prevue:
            bac_cible = None
        if not bac_cible:
            index:int = len(bacs)+1
            new_nom = "B" +str(index)
            new_bac = Bac(new_nom , first_bac.getSurface())
            if new_bac.getSurfaceDispo() >= surface_prevue:
                new_bac.addOb(ob)
                bacs.append(new_bac)
        else:
            bac_cible.addOb(ob)
    return bacs             