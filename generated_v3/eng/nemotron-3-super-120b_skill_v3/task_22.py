from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# Build Al(111) slab: 3 layers, 2x2 surface cell, 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Get N2 molecule
n2 = molecule('N2')

# Adsorb N2 on bridge site at height 2.0 Å (in-place modification)
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Assign EMT calculator (suitable for Al)
slab.calc = EMT()

# Output atom count and types
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {set(slab.get_chemical_symbols())}")
