from ase.build import bulk
from ase.calculators.emt import EMT

# Create a silicon bulk with diamond structure
si_bulk = bulk('Si', 'diamond', a=5.43)

# Create a 3x3x3 supercell
supercell = si_bulk.repeat((3, 3, 3))

# Assign a calculator
supercell.set_calculator(EMT())

# Print the number of atoms and cell volume
print("Number of atoms:", len(supercell))
print("Cell volume:", supercell.get_volume())
