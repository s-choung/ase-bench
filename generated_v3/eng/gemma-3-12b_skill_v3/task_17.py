from ase import Atoms
from ase.build import surface
from ase.calculators.emt import EMT
import numpy as np

slab = surface('Cu', (2, 1, 1), layers=3, vacuum=10.0, a=3.6)
slab.calc = EMT()

print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
