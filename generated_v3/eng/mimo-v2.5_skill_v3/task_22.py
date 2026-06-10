from ase.build import fcc111, molecule, add_adsorbate
from ase import Atoms

# Create Al(111) slab: 3 layers, 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Get N2 molecule
n2 = molecule('N2')

# Adsorb N2 on bridge site at height 2.0 Å
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Print results
print(f"Total atoms: {len(slab)}")
symbols = slab.get_chemical_symbols()
print(f"Atom types: {symbols}")
print(f"Counts - Al: {symbols.count('Al')}, N: {symbols.count('N')}")
