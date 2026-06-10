import numpy as np
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create 4-layer Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Tag bottom 2 layers (tags=1) and top 2 layers (tags=0)
n_layers = 4
atoms_per_layer = len(slab) // n_layers
for i, atom in enumerate(slab):
    atom.tag = 1 if i < 2 * atoms_per_layer else 0

# Store initial positions of fixed atoms
fixed_mask = slab.get_tags() == 1
initial_fixed_positions = slab.get_positions()[fixed_mask].copy()

# Apply constraint to fix bottom 2 layers
constraint = FixAtoms(indices=[i for i, atom in enumerate(slab) if atom.tag == 1])
slab.set_constraint(constraint)

# Set calculator and run optimization
slab.calc = EMT()
dyn = BFGS(slab, trajectory='opt.traj')
dyn.run(fmax=0.01)

# Get final positions of fixed atoms
final_fixed_positions = slab.get_positions()[fixed_mask].copy()

# Compare and print results
print("Initial fixed atom positions:")
print(initial_fixed_positions)
print("\nFinal fixed atom positions:")
print(final_fixed_positions)
print("\nMaximum displacement of fixed atoms:")
print(np.max(np.linalg.norm(final_fixed_positions - initial_fixed_positions, axis=1)))
