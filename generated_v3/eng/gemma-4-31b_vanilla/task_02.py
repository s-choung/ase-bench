from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# Create Pt(111) slab: 4 layers, 2x2 surface area
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Adsorb CO on the ontop site
# CO is treated as a single unit; positions are relative to surface
add_adsorbate(slab, 'CO', height=2.0, position='ontop')

# Attach a built-in calculator
slab.calc = EMT()

# Print number of atoms
print(len(slab))
