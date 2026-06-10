from ase.build import fcc111, molecule
from ase.添加_adsorbate import add_adsorbate

# Create Pt(111) 4-layer slab with 10A vacuum
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Create CO molecule
co = molecule('CO')

# Adsorb CO on the ontop site
add_adsorbate(slab, co, height=1.8, position='ontop')

# Print the number of atoms in the final structure
print(len(slab))
