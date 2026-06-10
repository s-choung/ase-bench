from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.visualize import view

# Create a Cu(100) surface with 3 layers
surface = fcc111('Cu', size=(3, 3, 3), vacuum=12.0)

# Print the number of atoms
print(f"Number of atoms: {len(surface)}")

# Print the cell information
print("Cell information:")
print(surface.get_cell())

# Set the calculator
surface.calc = EMT()

# Visualize the surface (optional)
# view(surface)
