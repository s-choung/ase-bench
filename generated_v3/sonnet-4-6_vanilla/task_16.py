from ase.build import bcc110
from ase.calculators.emt import EMT

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

print(f"원자 수: {len(slab)}")
print(f"Cell 크기: {slab.cell}")
print(f"Cell 파라미터 (a, b, c): {slab.cell.lengths()}")
