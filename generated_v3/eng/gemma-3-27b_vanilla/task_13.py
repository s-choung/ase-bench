from ase.build import bulk
from ase.calculators.emt import EMT

si = bulk('Si', crystalstructure='diamond', a=5.43)
supercell = si * [3, 3, 3]

print(len(supercell))
print(supercell.get_volume())
