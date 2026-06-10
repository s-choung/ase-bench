from ase.build import bulk, surface
from ase.calculators.emt import EMT

# Create Cu bulk and cut (2,1,1) surface
cu_bulk = bulk('Cu', 'fcc', a=3.615)
slab = surface(cu_bulk, (2, 1, 1), layers=3)
slab.center(vacuum=10, axis=2)

# Set calculator (EMT for demonstration)
slab.calc = EMT()

# Print information
print(f"Number of atoms: {len(slab)}")
print("Cell vectors:")
print(slab.get_cell())
