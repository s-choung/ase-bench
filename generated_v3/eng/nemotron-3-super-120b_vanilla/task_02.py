from ase.build import surface, molecule, add_adsorbate

# Pt(111) slab, 4 layers, 10 Å vacuum
slab = surface('Pt', (1, 1, 1), layers=4, vacuum=10.0)

# CO molecule
co = molecule('CO')

# Adsorbate CO on ontop site (position (0,0) in scaled coordinates) at ~1.2 Å height
add_adsorbate(slab, co, height=1.2, position=(0, 0))

# Print total number of atoms
print(len(slab))
