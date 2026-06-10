from ase.build import bcc110
from ase.calculators.emt import EMT

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10)
slab.calc = EMT()

print(f"Number of atoms: {len(slab)}")
print(f"Cell size: {slab.cell.cellpar()}")
