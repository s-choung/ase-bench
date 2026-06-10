from ase.build import bcc110
from ase.calculators.emt import EMT

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

print(f"원자 수: {len(slab)}")
print(f"Cell 크기: {slab.get_cell_lengths_and_angles()}")
print(f"Cell:\n{slab.get_cell()}")
