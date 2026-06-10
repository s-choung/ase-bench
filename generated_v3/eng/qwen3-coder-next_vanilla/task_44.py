from ase import Atoms, Atom
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Create Cu(111) 4-layer slab
slab = fcc111('Cu', a=3.61, layers=4, vacuum=10.0)

# Tag atoms: bottom 2 layers (z < 5.0 Å) get tag=1, top 2 layers get tag=0
for atom in slab:
    if atom.z < 5.0:
        atom.tag = 1
    else:
        atom.tag = 0

# Fix bottom 2 layers (tag=1)
constraint = FixAtoms(mask=[atom.tag == 1 for atom in slab])
slab.set_constraint(constraint)

# Set EMT calculator
slab.set_calculator(EMT())

# Store coordinates of fixed atoms before optimization
fixed_indices = [i for i, atom in enumerate(slab) if atom.tag == 1]
initial_coords = slab.get_positions()[fixed_indices]

# Optimization
optimizer = BFGS(slab)
optimizer.run(fmax=0.01)

# Get coordinates after optimization
final_coords = slab.get_positions()[fixed_indices]

# Print comparison
print("Fixed atoms coordinates (z < 5.0 Å):")
print("Before optimization:")
for i, pos in enumerate(initial_coords):
    print(f"Atom {i}: {pos}")
print("\nAfter optimization:")
for i, pos in enumerate(final_coords):
    print(f"Atom {i}: {pos}")
    
# Verify they didn't move
if np.allclose(initial_coords, final_coords):
    print("\nFixed atoms did not move during optimization (as expected).")
else:
    print("\nWARNING: Fixed atoms moved during optimization!")
