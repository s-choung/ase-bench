from ase.build import bulk, surface, add_vacuum
from ase.calculators.emt import EMT

# Create Cu bulk and cut (2,1,1) surface
cu_bulk = bulk('Cu', 'fcc', a=3.615)
slab = surface(cu_bulk, (2, 1, 1), layers=3)

# Add vacuum
add_vacuum(slab, 10.0)

# Set calculator
slab.calc = EMT()

# Print information
print(f"Number of atoms: {len(slab)}")
print(f"Cell vectors:\n{slab.get_cell()}")
print(f"Cell lengths and angles: {slab.get_cell_lengths_and_angles()}")
