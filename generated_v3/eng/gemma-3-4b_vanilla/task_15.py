from ase import Atoms
from ase.build import surface
from ase.calculators import EMT
from ase.io import write

# Create Cu(100) surface with 3 layers
surf = surface.Cu(100, depth=3, size=(3, 3, 3))

# Set vacuum
surf.vacuum = 12.0

# Set calculator
surf.set_calculator(EMT())

# Print number of atoms
print(len(surf))

# Print cell info
print(surf.cell)

# Write to file
write("cu100_3layer.xyz", surf)
