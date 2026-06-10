import numpy as np
from ase.build import fcc111, molecule, add_adsorbate

# Create Al(111) 3-layer slab
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Create N2 molecule
n2 = molecule('N2')

# Place N2 on bridge site at 2.0 Å height
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Print structure info
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {', '.join(set(slab.get_chemical_symbols()))}")
