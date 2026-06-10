from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# Create Pt(111) slab: 4 layers, 2x2 size, 10A vacuum
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Create CO molecule
co = molecule('CO')

# Adsorb CO on top site at height 1.8A
add_adsorbate(slab, co, height=1.8, position='ontop')

# Set calculator (required for potential energy/forces, though not explicitly asked for calculation here)
slab.calc = EMT()

print(len(slab))
