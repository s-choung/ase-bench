from ase import Atoms
from ase.geometry import get_distances

positions = [[0.0, 0.0, 0.0], [-1.16, 0.0, 0.0], [1.16, 0.0, 0.0]]
atoms = Atoms('CO2', positions=positions, cell=[10, 10, 10], pbc=False)
dists, _ = get_distances(atoms.positions, cell=atoms.cell, pbc=atoms.pbc)
print(dists)
