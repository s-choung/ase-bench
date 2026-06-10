from ase import Atoms
import numpy as np

positions = [(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)]
atoms = Atoms('CO2', positions=positions, cell=[10]*3, pbc=False)
print(atoms.get_distances(0, [1, 2]))
print(atoms.get_distances(1, [2]))
