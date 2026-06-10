from ase import Atoms
from ase.build import fcc100
from ase.build import add_vacuum
from ase.calculators.emt import EMT

slab = fcc100('Cu', size=(3,3,3))
slab = add_vacuum(slab, 12.0)
slab.set_calculator(EMT())

print("Number of atoms:", len(slab))
print("Cell info:")
print(slab.cell)
