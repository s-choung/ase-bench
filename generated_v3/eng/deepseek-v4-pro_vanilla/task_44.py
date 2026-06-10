import numpy as np
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Create 4-layer Cu(111) slab (2x2 surface unit cell)
atoms = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Tag bottom two layers (0) and top two layers (1) based on z-coordinate
z_unique = sorted(set(atoms.positions[:, 2]))
bottom_z = z_unique[:2]                     # two lowest z values
tags = [0 if pos[2] in bottom_z else 1 for pos in atoms.positions]
atoms.set_tags(tags)

# Identify fixed atoms (tag == 0) and save their initial positions
fixed_mask = np.array([atom.tag == 0 for atom in atoms])
initial_positions = atoms.positions[fixed_mask].copy()

# Apply FixAtoms constraint using the mask
constraint = FixAtoms(mask=fixed_mask)
atoms.set_constraint(constraint)

# Assign EMT calculator and run BFGS optimization
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Get final positions of fixed atoms
final_positions = atoms.positions[fixed_mask]

# Print comparison
print("Initial fixed atom positions:")
print(initial_positions)
print("\nFinal fixed atom positions:")
print(final_positions)

displacement = np.abs(final_positions - initial_positions).max()
print(f"\nMaximum displacement of fixed atoms: {displacement:.6f} Å")
