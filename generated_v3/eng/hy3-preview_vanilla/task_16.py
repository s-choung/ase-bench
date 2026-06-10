from ase.build import bulk, surface
from ase.visualize import view

# Create BCC Fe bulk
fe_bulk = bulk('Fe', 'bcc', a=2.87)

# Build (110) surface with 4 layers
slab = surface(fe_bulk, (1, 1, 0), 4, vacuum=10)

# Set supercell size
slab = slab.repeat((2, 2, 1))

# Output information
print(f"Number of atoms: {len(slab)}")
print(f"Cell size [Å]:")
print(slab.get_cell())
