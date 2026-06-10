from ase import Atoms
from ase.build import fcc111, add_adsorbate, molecule
from ase.visualize import view

# Create Al(111) slab with 3 layers and 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Get N2 molecule
n2 = molecule('N2')

# Add N2 on bridge site at height 2.0 Å
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Print number of atoms and atom types
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {set(slab.get_chemical_symbols())}")
