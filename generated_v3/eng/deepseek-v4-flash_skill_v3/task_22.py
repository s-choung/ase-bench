from ase.build import fcc111, add_adsorbate
from ase.build import molecule
from ase import Atoms

# Create Al(111) slab: 3 layers, vacuum 10 Å
slab = fcc111('Al', size=(1, 1, 3), a=4.05, vacuum=10.0)

# Create N2 molecule
n2 = molecule('N2')

# Adsorb N2 on bridge site at height 2.0 Å (center of mass)
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Print info
print('Number of atoms:', len(slab))
symbols = slab.get_chemical_symbols()
print('Atom types:', sorted(set(symbols)))
