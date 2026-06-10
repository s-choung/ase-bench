from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Create slab with tags
slab = fcc111('Cu', size=(4,4,4), vacuum=10.0, orthogonal=True)
slab.set_tags(range(len(slab)))

# Assign calculator
slab.calc = EMT()

# Constrain bottom 2 layers
fixed_mask = [z < 4.8 for z in slab.positions[:,2]]
slab.set_constraint(FixAtoms(mask=fixed_mask))

# Store initial positions
initial_positions = slab.get_positions()[fixed_mask]

# Optimize structure
BFGS(slab).run(fmax=0.01)

# Compare fixed atoms
final_positions = slab.get_positions()[fixed_mask]
print("Max displacement:", np.abs(initial_positions - final_positions).max())
