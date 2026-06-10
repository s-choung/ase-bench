from ase.lattice.surface import bcc110
from ase.calculators.emt import EMT

# Create Fe BCC(110) surface with 4 layers
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# Print results
print(f"Number of atoms: {len(slab)}")
print(f"Cell dimensions: {slab.get_cell()}")
