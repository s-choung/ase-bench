from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# Create Pt(111) 4-layer slab with 4x4 surface unit cell and 10 A vacuum
slab = fcc111('Pt', size=(4, 4, 4), vacuum=10)

# Add CO on top site (CO oriented along surface normal, C down)
add_adsorbate(slab, 'C', height=1.1, position='ontop')

# Optional: attach calculator (not needed for counting atoms but good practice)
slab.calc = EMT()

print(len(slab))
