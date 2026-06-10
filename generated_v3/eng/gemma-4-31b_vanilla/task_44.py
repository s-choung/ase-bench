import numpy as np
from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Create Cu(111) slab: 4 layers
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)

# Tag the bottom 2 layers (indices 0 to (num_atoms/2)-1 for this specific geometry)
# In fcc111 size=(3,3,4), total atoms = 3*3*4 = 36. Bottom 2 layers = 18 atoms.
# The build function orders by layer.
for atom in slab.atoms:
    if atom.index < 18:
        atom.set_tag('fixed')

# Identify indices of tagged atoms
fixed_indices = [atom.index for atom in slab if atom.tag == 'fixed']
c = FixAtoms(indices=fixed_indices)
slab.set_constraint(c)

# Store coordinates for verification
coords_before = slab.get_positions()[fixed_indices].copy()

# Optimization
slab.set_calculator(EMT())
opt = BFGS(slab)
opt.run(fmax=0.05)

coords_after = slab.get_positions()[fixed_indices]

print("Coordinates of fixed atoms before:\n", coords_before)
print("\nCoordinates of fixed atoms after:\n", coords_after)
print("\nMax difference:", np.max(np.abs(coords_before - coords_after)))
