from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# 4-layer Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=3.6)

# Fix bottom two layers (tags 3 and 4)
mask = [atom.tag >= 3 for atom in slab]
fixed_indices = [i for i, m in enumerate(mask) if m]
slab.set_constraint(FixAtoms(mask=mask))

# Store positions of fixed atoms before optimisation
initial_fixed = slab.positions[fixed_indices].copy()

# Optimise with EMT
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Positions after optimisation
final_fixed = slab.positions[fixed_indices]

# Compare
displacements = np.linalg.norm(final_fixed - initial_fixed, axis=1)
max_disp = np.max(displacements)
print(f"Maximum displacement of fixed atoms: {max_disp:.6f} Å")

print("\nInitial vs Final Coordinates of Fixed Atoms:")
print(f"{'Index':<6} {'Initial (x, y, z)':<36} {'Final (x, y, z)':<36} {'Displacement (Å)':<15}")
for idx, (i, f) in enumerate(zip(initial_fixed, final_fixed)):
    d = displacements[idx]
    print(f"{fixed_indices[idx]:<6} "
          f"({i[0]:10.6f} {i[1]:10.6f} {i[2]:10.6f})  "
          f"({f[0]:10.6f} {f[1]:10.6f} {f[2]:10.6f})  "
          f"{d:.6f}")
