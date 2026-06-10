from ase.build import fcc100
from ase.calculators.emt import EMT
from ase.units import Bohr

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12*Bohr)

print(f"Number of atoms: {len(slab)}")
print(slab.get_cell_lengths_and_angles())
slab.calc = EMT()
