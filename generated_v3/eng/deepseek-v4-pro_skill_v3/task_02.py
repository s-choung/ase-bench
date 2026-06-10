from ase.build import fcc111, add_adsorbate, molecule

# Create Pt(111) 4-layer slab with vacuum
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Adsorb CO on ontop site
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Print number of atoms in final structure
print(len(slab))
