from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

atoms = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)

# Set tags for the bottom 2 layers (tags 0 and 1)
for i, atom in enumerate(atoms):
    if atom.position[2] < atoms.cell[2, 2] / 2:
        atom.tag = 0
    else:
        atom.tag = 2

# Create FixAtoms constraint for the first two layers (tags 0 or 1)
constraint = FixAtoms(mask=[atom.tag < 2 for atom in atoms])
atoms.set_constraint(constraint)

# Set calculator and run optimization
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.02)

# Store initial coordinates of fixed atoms
initial_coords = []
for atom in atoms:
    if atom.tag < 2:
        initial_coords.append(atom.position.copy())

# Store final coordinates of fixed atoms
final_coords = []
for atom in atoms:
    if atom.tag < 2:
        final_coords.append(atom.position.copy())

# Compare coordinates
print("Initial coordinates of fixed atoms:")
for i, coords in enumerate(initial_coords):
    print(f"Atom {i}: {coords}")

print("\nFinal coordinates of fixed atoms:")
for i, coords in enumerate(final_coords):
    print(f"Atom {i}: {coords}")

# Calculate and print the maximum difference in coordinates
diffs = np.array(initial_coords) - np.array(final_coords)
max_diff = np.max(np.abs(diffs))
print(f"\nMaximum difference in coordinates (should be close to zero): {max_diff}")
