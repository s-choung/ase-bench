from ase.build import fcc111, molecule, add_adsorbate
from ase import Atoms

# Create Al(111) 3-layer slab
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Get N2 molecule
n2 = molecule('N2')

# Adsorb N2 on bridge site at height 2.0 angstroms
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Print number of atoms
print(f"Number of atoms: {len(slab)}")

# Print atom types
atom_types = set(slab.get_chemical_symbols())
print(f"Atom types: {atom_types}")
