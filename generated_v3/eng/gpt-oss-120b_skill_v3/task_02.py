from ase.build import fcc111, add_adsorbate, molecule

# 4‑layer Pt(111) slab with 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# CO molecule
co = molecule('CO')

# Place CO on an ontop site (height ≈ 1.85 Å)
add_adsorbate(slab, co, height=1.85, position='ontop')

# Output total atom count
print(slab.get_number_of_atoms())
