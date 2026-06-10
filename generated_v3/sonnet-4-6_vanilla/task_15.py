from ase.build import fcc100
from ase.calculators.emt import EMT

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

calc = EMT()
slab.calc = calc

print(f"원자 수: {len(slab)}")
print(f"Cell:\n{slab.cell}")
print(f"Cell 크기 (Å): a={slab.cell[0][0]:.4f}, b={slab.cell[1][1]:.4f}, c={slab.cell[2][2]:.4f}")
print(f"원자 위치:\n{slab.positions}")
