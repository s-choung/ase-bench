from ase.build import fcc100
from ase.calculators.emt import EMT

# Create a Cu(100) surface with 3 layers
slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

# Assign EMT calculator
slab.calc = EMT()

# Print number of atoms and cell information
print("Number of atoms:", len(slab))
print("Cell info:\n", slab.get_cell())
