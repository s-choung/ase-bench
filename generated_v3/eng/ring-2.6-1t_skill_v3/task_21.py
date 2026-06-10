from ase.cluster import Icosahedron
from ase import Atoms
import numpy as np

atoms = Icosahedron('Au', 3)
print(f'Number of atoms: {len(atoms)}')
com = np.average(atoms.get_positions(), axis=0, weights=atoms.get_masses())
print(f'Center of mass: {com}')
