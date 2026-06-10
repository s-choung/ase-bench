from ase import Atoms
from ase.geometry import get_distances

atoms = Atoms('CO2', positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]], cell=[10, 10, 10], pbc=False)
dist_matrix, _ = get_distances(atoms.positions, atoms.positions, cell=atoms.cell, pbc=atoms.pbc)
print(dist_matrix)
