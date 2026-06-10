from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Create a 4-layer Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)

# Tag the bottom 2 layers
for atom in slab[:6]:  # 3x2 = 6 atoms in the bottom 2 layers
    atom.tag = 1

# Apply FixAtoms constraint
slab.set_constraint(FixAtoms(mask=slab.get_tags()))

# Attach EMT calculator
slab.set_calculator(EMT())

# Store initial coordinates of fixed atoms
initial_coords = slab[slab.get_tags() == 1].positions.copy()

# Perform BFGS optimization
dyn = BFGS(slab, trajectory='cu_opt.traj')
dyn.run(fmax=0.01)

# Get final coordinates of fixed atoms
final_coords = slab[slab.get_tags() == 1].positions

# Compare and print coordinates
print("Initial coordinates of fixed atoms:")
print(initial_coords)
print("\nFinal coordinates of fixed atoms:")
print(final_coords)
