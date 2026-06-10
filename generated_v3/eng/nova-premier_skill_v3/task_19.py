from ase import Atoms
from ase.geometry import get_distances

# Manually build CO2
cell = [[10,0,0], [0,10,0], [0,0,10]]
atoms = Atoms('COO', positions=[(0,0,0), (1.16,0,0), (-1.16,0,0)], cell=cell, pbc=False)

# Calculate distances
pairs = [[0,1], [0,2], [1,2]]
d = get_distances(atoms.get_positions(), pairs, cell, pbc=False)
print("CO distances (Å):", d[0], d[1])
print("OO distance (Å):", d[2])
