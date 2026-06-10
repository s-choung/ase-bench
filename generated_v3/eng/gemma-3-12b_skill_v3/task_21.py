from ase import Atoms
from ase.cluster import Icosahedron
import numpy as np

atoms = Icosahedron('Au', length=5, noshells=3)

print(f"Number of atoms: {len(atoms)}")
print(f"Center of mass: {atoms.get_center_of_mass()}")
