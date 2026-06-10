import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Create 4-layer Cu(111) slab
atoms = fcc111('Cu', size=(4,4,4), vacuum=10.0)

# Assign tags to bottom 2 layers (fixed)
unique_z = sorted(np.unique(atoms.positions[:, 2]))
atoms.set_tags(np.where(np.isin(atoms.positions[:, 2], unique_z[:2]), 1, 0))
fixed_idx = [i for i, tag in enumerate(atoms.get_tags()) if tag == 1]

# Apply fixed atom constraint
atoms.set_constraint(FixAtoms(indices=fixed_idx))

# Set up calculator and save initial fixed atom positions
atoms.calc = EMT()
initial_fixed = atoms.positions[fixed_idx].copy()

# Run BFGS optimization
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Verify fixed atoms did not move
final_fixed = atoms.positions[fixed_idx]
print("\nFixed atom initial coordinates (Å):\n", np.round(initial_fixed, 6))
print("\nFixed atom final coordinates (Å):\n", np.round(final_fixed, 6))
print(f"\nMaximum displacement of fixed atoms (Å): {np.max(np.abs(final_fixed - initial_fixed)):.10f}")
