from ase import Atoms
from ase.build import fcc111
import numpy as np

# Create a Si bulk with diamond structure
a = 5.43  # Lattice constant in Angstroms
atoms = fcc111('Si', size=3, latticeconstant=a)

# Print the number of atoms
print(len(atoms))

# Calculate the cell volume
cell_volume = atoms.get_cell_volume()
print(cell_volume)
