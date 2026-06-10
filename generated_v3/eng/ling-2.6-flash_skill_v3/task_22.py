from ase import units
from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms

slab = fcc111('Al', size=(1, 1, 3), vacuum=10.0, a=4.05)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')
slab.set_constraint(FixAtoms(mask=[a.index >= 3 for a in slab]))

print('Number of atoms:', len(slab))
print('Atom types:', set(a.symbol for a in slab))
