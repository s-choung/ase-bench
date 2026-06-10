from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.build import molecule
from ase.calculators.emt import EMT

# Create Al(111) slab: 3 layers, 2x2 surface unit cell
slab = fcc111('Al', indices=(1, 1, 1), size=(2, 2, 3), vacuum=10.0)

# Define N2 molecule
n2 = molecule('N2')

# Adsorb N2 at bridge site (height 2.0 A)
# Bridge site in fcc111 surface is typically between two atoms on the top layer
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Attach EMT calculator
slab.set_calculator(EMT())

# Output results
print(f"Total atoms: {len(slab)}")
print(f"Atom types: {[atom.symbol for atom in slab.get_chemical_symbols()]}")
