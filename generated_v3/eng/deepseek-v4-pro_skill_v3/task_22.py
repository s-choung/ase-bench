from ase.build import fcc111, molecule, add_adsorbate
from collections import Counter

# Create Al(111) 3-layer slab with 10 Å vacuum
slab = fcc111('Al', size=(1, 1, 3), vacuum=10.0)

# Add N2 molecule on bridge site at 2.0 Å height
add_adsorbate(slab, molecule('N2'), height=2.0, position='bridge')

# Print info
print(f"Number of atoms: {len(slab)}")
print("Atom types:", dict(Counter(slab.get_chemical_symbols())))
