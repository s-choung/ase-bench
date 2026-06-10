from ase.build import fcc111, add_adsorbate, add_vacuum
from ase import molecule

# Pt(111) slab, 4 layers, 2×2 surface cell
slab = fcc111('Pt', size=(2, 2, 4), vacuum=0.0)

# add 10 Å vacuum
add_vacuum(slab, 10.0)

# CO adsorbate on ontop site
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# number of atoms after adsorption
print(slab.get_number_of_atoms())
