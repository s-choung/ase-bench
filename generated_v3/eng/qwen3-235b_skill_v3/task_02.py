from ase.build import fcc111, molecule, add_adsorbate, add_vacuum
from ase.calculators.emt import EMT

# Create Pt(111) slab with 4 layers
slab = fcc111('Pt', size=(1, 1, 4))

# Add vacuum
add_vacuum(slab, 10.0)

# Create CO molecule and adsorb on ontop site
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Print number of atoms
print(len(slab))
