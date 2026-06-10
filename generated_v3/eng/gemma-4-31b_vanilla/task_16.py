from ase.build import fcc110, bcc110
from ase.calculators.emt import EMT

# Create Fe BCC(110) surface
# size=(2,2,4) refers to the repetition of the surface unit cell
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# Assign built-in EMT calculator
slab.calc = EMT()

# Print required information
print(f"Number of atoms: {len(slab)}")
print(f"Cell size: {slab.get_cell().arrays}")
