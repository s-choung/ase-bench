from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

# Create a 4-layer Pt(111) slab
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Add a CO molecule and place it on top of the surface
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Set up the calculator
slab.set_calculator(EMT())

# Fix the bottom two layers
constraint = FixAtoms(mask=[atom.symbol == 'Pt' and atom.tag <= 2 for atom in slab])
slab.set_constraint(constraint)

# Output the number of atoms
print('Number of atoms:', len(slab))
