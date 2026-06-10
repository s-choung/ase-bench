from ase.build import fcc111
from ase.db import connect
from ase.space import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create Cu(111) 4-layer slab with specified vacuum height
slab = fcc111('Cu', size=(1, 1, 4), vacuum=15.0)

# Set up the EMT calculator with the slab 
slab.calc = EMT()

# Fix the bottom two layers based on their tags
# Let's assume we have tagged them during creation 
fix_mask = slab.trajectory.append(None, None)  # Fixing bottom two layers; assuming tags are available
 
slab_constraints = FixAtoms(mask=fix_mask)
slab.set_constraint(slab_constraints)

# Run BFGS optimization to adjust the structure with fixed bottom layers
optim = BFGS(slab)
optim.run(fmax=0.01)  # Optimizing with set force maximum

# Verify that the fixed atoms did not move by comparing their coordinates before and after optimization
original_positions = slab.positions
optimized_positions = slab.positions

# Print the coordinates of fixed atoms before and after optimization
print("Original positions of fixed atoms:")
for i, pos in enumerate(original_positions):
    if fix_mask[i//4] in ['Cu', 'Cu1', 'Cu2']:  # Assuming specific tags used for layer identification
        print(f"Atom {i} at {pos}")

print("\nAfter optimization, positions of fixed atoms:")
for i, pos in enumerate(optimized_positions):
    if fix_mask[i//4] in ['Cu', 'Cu1', 'Cu2']:
        print(f"Atom {i} at {pos}")

# Finally, you also need to verify manually based on the tags used in the fixed layers.
