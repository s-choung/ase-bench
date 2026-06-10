from ase.build import fcc111, molecule, add_adsorbate
from ase.symbols import symbols2numbers

slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)
n2 = molecule('N2')
n2.rotate(90, 'x', rotate_cell=False)

add_adsorbate(slab, n2, height=2.0, position='bridge')

print('Number of atoms:', len(slab))
print('Atom types:', slab.get_chemical_symbols())
