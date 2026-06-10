from ase import Atoms
from ase.build import fcc111, molecule
from ase.build import add_adsorbate, add_vacuum
from ase.calculators.emt import EMT

# Create Al(111) 3-layer slab with vacuum
slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)

# Add N2 molecule on bridge site
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Print number of atoms and types
print(f"Total atoms: {len(slab)}")
types = set(slab.get_chemical_symbols())
print(f"Atom types: {sorted(types)}")
