from ase.build import fcc111, molecule, add_adsorbate

# Create Pt(111) slab: 2x2 surface, 4 layers, 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Create CO molecule
co = molecule('CO')

# Add CO on ontop site (default position) with 1.8 Å height
add_adsorbate(slab, co, height=1.8, position='ontop')

# Print number of atoms
print(f"Total atoms: {len(slab)}")
