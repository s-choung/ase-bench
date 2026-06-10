from ase.build import fcc111, molecule
from ase.build import add_adsorbate
from ase.calculators.emt import EMT

# Create Al(111) 3-layer slab with 10A vacuum
slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)

# Get N2 molecule
n2 = molecule('N2')

# Adsorb N2 on bridge site at 2.0A height
# 'bridge' position is supported by add_adsorbate
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Set calculator
slab.calc = EMT()

# Print results
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {slab.get_chemical_symbols()}")
