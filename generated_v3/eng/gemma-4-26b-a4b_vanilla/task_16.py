from ase.build import bulk, surface
from ase.calculators.emt import EMT

# Create Fe BCC bulk
atoms = bulk('Fe', 'bcc', a=2.866)

# Create (110) surface, 4 layers, size=(2,2,4)
# Note: size=(2,2) refers to the lateral expansion of the unit cell
surf = surface(atoms, (1, 1, 0), layers=4, vacuum=10.0)
surf = surf.repeat((2, 2, 1))

# Apply calculator
surf.set_calculator(EMT())

# Print required info
print(f"Number of atoms: {len(surf)}")
print(f"Cell size: {surf.get_cell().cellSize()}")
