from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# Pt(111) slab, 4 layers, 10 Å vacuum
slab = fcc111('Pt', size=(1, 1, 4), vacuum=10, orthogonal=True)

# CO molecule
co = molecule('CO')

# place CO on an ontop site (above the top‑layer atom)
top = slab[-1]                     # a surface atom
add_adsorbate(slab, co, height=1.8, position=(top.x, top.y))

# optional calculator (built‑in)
slab.set_calculator(EMT())

print(len(slab))   # number of atoms in the final structure
