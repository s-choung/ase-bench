from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Create Cu(111) slab with 4 layers and vacuum
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Set tags: bottom 2 layers = 1, top 2 layers = 2
for i, atom in enumerate(slab):
    atom.tag = 1 if i < 8 else 2  # 2x2=4 atoms per layer, so 8 atoms in bottom 2 layers

# Record initial positions of fixed atoms
initial_pos = slab.positions[slab.get_tags() == 1].copy()

# Apply constraint to fix bottom 2 layers
slab.set_constraint(FixAtoms(mask=(slab.get_tags() == 1)))

# Set calculator and optimize
slab.calc = EMT()
BFGS(slab).run(fmax=0.01)

# Get final positions of fixed atoms
final_pos = slab.positions[slab.get_tags() == 1]

# Verify fixed atoms did not move
print("Initial positions of fixed atoms:")
print(initial_pos)
print("\nFinal positions of fixed atoms:")
print(final_pos)
print(f"\nMax displacement of fixed atoms: {np.max(np.abs(final_pos - initial_pos)):.2e} Å")
