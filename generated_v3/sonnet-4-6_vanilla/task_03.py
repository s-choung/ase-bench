from ase import Atoms
from ase.build import mx2

mos2 = mx2(formula='MoS2', kind='2H', a=3.16, thickness=3.172, size=(1,1,1), vacuum=10.0)

print("Cell size:")
print(mos2.get_cell())
print(f"\nCell parameters (a, b, c): {mos2.cell.lengths()}")
print(f"Number of atoms: {len(mos2)}")
print(f"Chemical formula: {mos2.get_chemical_formula()}")
