from ase.build import fcc100
from ase.calculators.emt import EMT

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

print(f"원자 수: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
print(f"Cell lengths and angles: {slab.get_cell_lengths_and_angles()}")
print(f"PBC: {slab.get_pbc()}")
