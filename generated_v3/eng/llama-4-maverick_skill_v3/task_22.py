from ase import Atoms
from ase.build import fcc111, add_adsorbate, molecule, add_vacuum

slab = fcc111('Al', size=(2,2,3), a=4.05)
add_vacuum(slab, 10)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {set(slab.get_chemical_symbols())}")
