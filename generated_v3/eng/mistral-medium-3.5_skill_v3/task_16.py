from ase.build import bcc110
from ase.calculators.emt import EMT

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()
print(len(slab), slab.get_cell_lengths_and_angles())
