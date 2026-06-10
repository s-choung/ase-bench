from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
import numpy as np

# Create diamond structure Si bulk with lattice constant 5.43 Å
a = 5.43
si_bulk = bulk('Si', 'diamond', a=a)

# Create 3x3x3 supercell
si_supercell = si_bulk * (3, 3, 3)

# Print number of atoms and cell volume
num_atoms = len(si_supercell)
volume = si_supercell.get_volume()

print(f"Number of atoms: {num_atoms}")
print(f"Cell volume: {volume:.2f} Å^3")
