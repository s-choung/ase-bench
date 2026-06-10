from ase.build import fcc111, molecule, add_adsorbate, add_vacuum
from ase.calculators.emt import EMT

# Create Al(111) slab (3 layers)
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Get N2 molecule and adsorb on bridge site
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Set calculator (required for basic structural consistency)
slab.calc = EMT()

# Output final structure info
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {slab.get_chemical_symbols()}")
