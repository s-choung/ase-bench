from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# Create Cu(111) 4-layer slab and tag atoms by layer
atoms = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Tag atoms (layer 0: bottom, layer 3: top)
tags = np.zeros(len(atoms), int)
for i, atom in enumerate(atoms):
    z = atom.position[2]
    layer = int(round((z - atoms.get_cell()[2, 2]/2) / atoms.get_cell()[2, 2] * 4))  # Approximate layer
    layer = max(0, min(3, layer))  # Clamp to [0,3] range
    tags[i] = layer
atoms.set_tags(tags)

# Fix bottom 2 layers (tags 0 and 1)
constraint = FixAtoms(mask=[tag < 2 for tag in tags])
atoms.set_constraint(constraint)

# Save initial positions of fixed atoms
fixed_init = [atom.position.copy() for i, atom in enumerate(atoms) if tags[i] < 2]

# Set calculator and optimize
atoms.calc = EMT()
opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.01)

# Check fixed atoms after optimization
fixed_final = [atom.position for i, atom in enumerate(atoms) if tags[i] < 2]

# Verify and print comparisons
print("Fixed atoms verification (difference < 1e-6):")
all_fixed = True
for i, (init, final) in enumerate(zip(fixed_init, fixed_final)):
    diff = np.linalg.norm(init - final)
    if diff > 1e-6:
        all_fixed = False
    print(f"Atom {i}: difference = {diff:.2e}")

print(f"\nAll fixed atoms remained stationary: {all_fixed}")
