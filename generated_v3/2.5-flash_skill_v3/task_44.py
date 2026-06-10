from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

fixed_mask = [atom.tag < 2 for atom in slab]
fixed_indices = [atom.index for atom in slab if atom.tag < 2]

initial_fixed_positions = slab.positions[fixed_indices].copy()

slab.set_constraint(FixAtoms(mask=fixed_mask))

slab.calc = EMT()

optimizer = BFGS(slab)
optimizer.run(fmax=0.05)

final_fixed_positions = slab.positions[fixed_indices]

print("Initial positions of fixed atoms (first 5 rows):")
print(initial_fixed_positions[:5])
print("\nFinal positions of fixed atoms (first 5 rows):")
print(final_fixed_positions[:5])

if np.allclose(initial_fixed_positions, final_fixed_positions, atol=1e-6):
    print("\nVerification: Positions of fixed atoms did NOT change during optimization.")
else:
    print("\nVerification: ERROR! Positions of fixed atoms CHANGED during optimization.")
