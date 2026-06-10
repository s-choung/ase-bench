from ase.build import fcc111, molecule
from ase.calculators.emt import EMT
from ase.build import add_adsorbate

# Pt(111) slab: 2x2 surface, 4 layers, 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# CO molecule
co = molecule('CO')

# Adsorbate CO on ontop site at 1.8 Å height
add_adsorbate(slab, co, height=1.8, position='ontop')

# Attach a calculator (EMT works for Pt and CO)
slab.calc = EMT()

# Print total number of atoms
print(len(slab))
