from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT

# Create Pt(111) 4-layer slab
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Adsorb CO molecule on the ontop site
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Fix bottom 2 layers
slab.set_constraint(FixAtoms(mask=[atom.tag < 2 for atom in slab]))

# Calculate with EMT calculator
slab.calc = EMT()

# Print the number of atoms in the final structure
print("Number of atoms in the final structure:", len(slab))
