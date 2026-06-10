from ase import Atoms
from ase.build import fcc111
from ase.visualize import view

# Create Fe BCC(110) surface with 4 layers
atoms = fcc111('Fe', size=(2, 2, 4), vacuum=10.0)

# Print the number of atoms
print(f"Number of atoms: {len(atoms)}")

# Print the cell size
cell_lengths = atoms.get_cell_lengths_and_angles()
print(f"Cell Size: a={cell_lengths[0]}, b={cell_lengths[1]}, c={cell_lengths[2]}")

# Visualize the structure
#view(atoms)
