from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Create Cu(111) slab with 4 layers
slab = fcc111('Cu', (2, 2, 4))

# Assign tags: 0 for fixed (bottom 2 layers), 1 for free
slab.set_tags([0 if atom.z < slab.positions[-4][2] else 1 for atom in slab])

# Fix bottom 2 layers
constraint = FixAtoms(indices=[atom.index for atom in slab if atom.tag == 0])
slab.set_constraint(constraint)

# EMT calculator
slab.calc = EMT()

# Save initial positions of fixed atoms
fixed_pos_before = slab.positions[slab.get_tags() == 0].copy()

# Optimize
opt = BFGS(slab)
opt.run(fmax=0.01)

# Compare fixed atoms' positions
fixed_pos_after = slab.positions[slab.get_tags() == 0]
print("Fixed atoms moved:", (fixed_pos_after - fixed_pos_before).any())
