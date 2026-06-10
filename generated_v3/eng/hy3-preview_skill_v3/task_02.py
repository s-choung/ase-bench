from ase.build import fcc111, molecule, add_adsorbate

# Create Pt(111) slab with 4 layers and 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Create CO molecule
co = molecule('CO')

# Adsorb CO on ontop site
add_adsorbate(slab, co, height=2.0, position='ontop')

# Print number of atoms in final structure
print(f"Number of atoms: {len(slab)}")
