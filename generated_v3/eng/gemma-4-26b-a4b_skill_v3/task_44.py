import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# 1. Build 4-layer Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
slab.calc = EMT()

# 2. Identify bottom 2 layers using Z-coordinates
# Get unique Z positions and select the lowest two
z_positions = sorted(list(set(atom.position[2] for atom in slab)))
bottom_z_threshold = z_positions[1]

# Assign tags: 1 for fixed (bottom 2 layers), 2 for mobile (top layers)
for atom in slab:
    if atom.position[2] <= bottom_z_threshold:
        atom.tag = 1
    else:
        atom.tag = 2

# 3. Record initial positions of fixed atoms
fixed_indices = [atom.index for atom in slab if atom.tag == 1]
initial_coords = slab.get_positions()[fixed_indices]

# 4. Apply FixAtoms constraint based on tags
constraint = FixAtoms(indices=fixed_indices)
slab.set_constraint(constraint)

# 5. Optimize structure
opt = BFGS(slab)
opt.run(fmax=0.05)

# 6. Verify results
final_coords = slab.get_positions()[fixed_indices]

print("Fixed Atoms Verification:")
print(f"Initial Coords:\n{initial_coords}")
print(f"Final Coords:\n{final_coords}")

# Check if the maximum displacement of fixed atoms is near zero
diff = np.abs(final_coords - initial_coords).max()
print(f"\nMax displacement of fixed atoms: {diff:.2e} Å")

if diff < 1e-5:
    print("SUCCESS: Fixed atoms did not move.")
else:
    print("FAILURE: Fixed atoms moved.")
