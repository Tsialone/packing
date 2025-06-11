from Bac import Bac
from Ob import Ob
from Fonction import ff1D , bf1D , wf1D
import random
import math
import copy
obs_val: list[float] = [2.89, 5.28, 1.85, 8.77, 1.32 ]
obs = []
i = 1
for ob_val in obs_val:
    ob = Ob("ob" + str(i), ob_val)
    obs.append(ob)
    i += 1

first_bac = Bac("B1", 10)
bacs_resp = ff1D(obs,  copy.deepcopy (first_bac))
print("\n--------------ff1d--------------")
for bac in bacs_resp:
    print(bac)

bacs_resp = bf1D(obs, copy.deepcopy (first_bac))
print("\n--------------bf1D--------------")
for bac in bacs_resp:
    print(bac)
    
bacs_resp = wf1D(obs, copy.deepcopy (first_bac))
print("\n--------------wf1D--------------")
for bac in bacs_resp:
    print(bac)





# print(first_bac.getSurface())
