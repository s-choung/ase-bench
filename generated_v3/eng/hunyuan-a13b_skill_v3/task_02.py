from ase.build import fcc111

# Create a Pt(111) slab
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Create a CO molecule
co = molecule('CO')

# Add CO to the slab on the ontop site
add_adsorbate(slab, co, height=1.8, position='ontop')

# Print the number of atoms in the final structure
print(len(slab))
