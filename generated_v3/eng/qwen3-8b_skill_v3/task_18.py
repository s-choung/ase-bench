import numpy as np
from ase import molecule

atoms = molecule('CH4')
print("Chemical formula:", atoms.get_chemical_formula())
print("Atomic coordinates (Å):\n", atoms.get_positions())
bond_lengths = [np.linalg.norm(atoms.positions[0] - atoms.positions[i]) for i in range(1, 5)]
print("Bond lengths (Å):", bond_lengths)
