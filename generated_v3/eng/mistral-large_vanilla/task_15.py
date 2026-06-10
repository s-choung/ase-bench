from ase.build import fcc100
from ase.calculators.emt import EMT

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12)
slab.calc = EMT()

print(f"Number of atoms: {len(slab)}")
print("Cell info:")
print(slab.cell)
