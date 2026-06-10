from ase.build import nanotube
from ase import Atoms
import numpy as np

atoms = nanotube(6, 6, length=4, bond=1.42, symbol='C')
atoms.center(vacuum=5.0, axis=(0, 1))
atoms.pbc = True

print(len(atoms))
print(atoms.get_cell_lengths_and_angles())
