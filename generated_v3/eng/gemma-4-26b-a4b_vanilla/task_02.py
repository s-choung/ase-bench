from ase.build import fcc111, add_adsorbate
from ase.visualize import view
from ase.calculators.emt import EMT
from ase.build import molecule

# Create 4-layer Pt(111) slab
slab = fcc111('Pt', size=(3, 3, 4), vacuum=10.0)

# Create CO molecule
co = molecule('CO')

# Adsorb CO on the ontop site of the top layer
# Site index 0 corresponds to the top layer atoms
add_adsorbate(slab, co, height=1.5, position='ontop')

# Set calculator (using EMT as a placeholder, though EMT is for small atoms)
# In real applications, one would use GPAW or VASP here.
for atom in slab:
    atom.calc = EMT()

print(len(slab))
