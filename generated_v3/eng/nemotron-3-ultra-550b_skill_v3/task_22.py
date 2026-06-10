from ase.build import fcc111, add_adsorbate, molecule
from ase import Atoms

# Create Al(111) 3-layer slab with 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Get N2 molecule
n2 = molecule('N2')

# Adsorb N2 on bridge site at 2.0 Å height
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Print number of atoms and atom types
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {slab.get_chemical_symbols()}")
