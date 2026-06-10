import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# 1. Setup Cu(111) slab
# Cu radius ~1.28 A, lattice constant ~3.61 A
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
slab.set_calculator(EMT())

# 2. Identify bottom 2 layers and apply FixAtoms
# Layers are distinguished by their z-coordinate
z_coords = slab.positions[:, 2]
z_threshold = np.percentile(z_coords, 25)  # Bottom 25% of atoms roughly equates to bottom 2/4 layers
indices_to_fix = [atom.index for atom in slab if atom.position[2] <= z_threshold]

constraint = FixAtoms(indices=indices_to_fix)
slab.set_constraint(constraint)

# 3. Store initial coordinates of fixed atoms
fixed_indices = constraint.get_indices()
initial_coords = slab.positions[fixed_indices].copy()

# 4. Structural optimization
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

# 5. Verification
final_coords = slab.positions[fixed_indices]

print(f"Fixed indices: {fixed_indices}")
print("\nInitial Coordinates (Fixed Atoms):")
print(initial_coords)
print("\nFinal Coordinates (Fixed Atoms):")
print(final_coords)

# Check if max displacement is negligible
diff = np.max(np.abs(final_coords - initial_coords))
print(f"\nMax displacement of fixed atoms: {diff:.2e} Å")

if diff < 1e-5:
    print("Verification SUCCESS: Fixed atoms did not move.")
else:
    print("Verification FAILURE: Fixed atoms moved.")
