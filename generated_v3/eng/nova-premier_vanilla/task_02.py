from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# Create Pt slab
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Add CO molecule
co = molecule('CO')
add_adsorbate(slab, co, height=1.5, position='ontop')

# Assign EMT calculator
slab.calc = EMT()

# Output atom count
print(len(slab))
