from ase.build import fcc111, molecule
from ase.calculators.emt import EMT
from ase import Atoms

slab = fcc111('Al', size=(2, 2, 3), vacuum=10)
n2 = molecule('N2')
n2.translate([2.5, 2.5, 2.0 + slab.positions[:, 2].max()])
system = slab + n2

print(f"Number of atoms: {len(system)}")
print(f"Atom types: {set(system.get_chemical_symbols())}")
