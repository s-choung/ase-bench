from ase.build import surface
from ase.build import add_vacuum
from ase.calculators.emt import EMT

# Create (2,1,1) surface with 3 layers
slab = surface('Cu', (2, 1, 1), 3)
add_vacuum(slab, 10.0)

print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
