from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT

a = 5.43
si = bulk('Si', 'diamond', a=a)
sc = si.repeat((3,3,3))

print("Number of atoms:", len(sc))
print("Cell volume:", sc.get_volume())
