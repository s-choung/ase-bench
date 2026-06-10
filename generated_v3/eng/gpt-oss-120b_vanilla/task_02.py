from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# Pt(111) slab: 2x2 surface, 4 layers, 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0, orthogonal=True)

# CO molecule
co = molecule('CO')
# Place CO on an ontop site (height ~1.85 Å)
add_adsorbate(slab, co, height=1.85, position='ontop')

# Simple calculator (optional)
slab.set_calculator(EMT())

print(len(slab))
