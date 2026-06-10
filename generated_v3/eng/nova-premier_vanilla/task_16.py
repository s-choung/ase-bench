from ase.build import bcc110
from ase.calculators.emt import EMT

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()
print("Number of atoms:", len(slab))
print("Cell size:", slab.cell.cellpar())
