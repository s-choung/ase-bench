from ase.build import fcc100
from ase.calculators.emt import EMT
from ase.visualize import view

# Create Cu(100) surface with 3 layers
# Note: EMT is for single atoms, but used here per instructions to satisfy "built-in calculator" requirement
slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)
slab.calc = EMT()

print(f"Number of atoms: {len(slab)}")
print(f"Cell information:\n{slab.get_cell()}")
print(f"Positions:\n{slab.get_positions()}")
