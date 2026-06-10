from ase import Atoms
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Create Cu(111) 4-layer slab with vacuum
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)

# Set calculator
slab.calc = EMT()

# Tag atoms: bottom 2 layers = tag 1, top 2 layers = tag 0
for atom in slab:
    if atom.z < slab.cell[2, 2] * 0.5:
        atom.tag = 1
    else:
        atom.tag = 0

# Print initial coordinates of fixed atoms (tag==1)
fixed_indices = [a.index for a in slab if a.tag == 1]
print("Fixed atoms initial coordinates (z-index):")
for idx in fixed_indices:
    print(f"  {idx}: {slab.positions[idx]}")

# Apply FixAtoms constraint to bottom 2 layers
constraint = FixAtoms(mask=[a.tag == 1 for a in slab])
slab.set_constraint([constraint])

# Optimize structure
opt = BFGS(slab, trajectory='slab_opt.traj')
opt.run(fmax=0.01)

# Print final coordinates of fixed atoms (should be unchanged)
print("\nFixed atoms final coordinates (z-index):")
for idx in fixed_indices:
    print(f"  {idx}: {slab.positions[idx]}")

# Verify no movement
initial_pos = np.array([slab.get_initial_positions()[idx] for idx in fixed_indices])
final_pos = np.array([slab.positions[idx] for idx in fixed_indices])
print("\nMovement verification (should be ~0):")
print("Max displacement:", np.max(np.abs(final_pos - initial_pos)))
