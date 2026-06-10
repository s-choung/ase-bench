from ase import Atoms
from ase.build import bulk
from ase.build import make_supercell
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
make_supercell(atoms, np.diag([2, 2, 2]))
cell = atoms.get_cell_lengths_and_angles()
print(f"Cell: {cell}")
print(f"Number of atoms: {len(atoms)}")
