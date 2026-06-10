from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT

slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)
add_adsorbate(slab, 'N2', height=2.0, position='bridge')
slab.set_calculator(EMT())
slab.constraints = [FixAtoms(mask=slab.numbers == 13)]

print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {set(slab.get_chemical_symbols())}")
