from ase.build import fcc111, molecule
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase import Atoms

# Create Pt(111) 4-layer slab
slab = fcc111('Pt', size=(3, 3, 4), vacuum=10.0, orthogonal=True)

# Fix all but topmost layer
mask = [atom.tag < 3 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# CO molecule, centered
co = molecule('CO')
co.rotate('x', 90)

# Place CO on ontop site of a top layer Pt atom
top_atom = [atom for atom in slab if atom.tag == 3][0]
z_offset = 1.85  # Approximate CO-Pt distance
co.translate(top_atom.position + (0, 0, z_offset) - co[0].position)

# Merge
system = slab + co

# Set calculator
system.calc = EMT()

print(len(system))
