from ase import Atoms
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Build Cu(111) 4-layer slab
slab = fcc111('Cu', size=(1,1,4), vacuum=10.0)

# Tag bottom 2 layers (0=fixed, 1=mobile)
unique_zs = sorted(np.unique(slab.get_positions()[:,2]))
fixed_zs = unique_zs[:2]
for atom in slab:
    atom.tag = 0 if atom.z in fixed_zs else 1

# Add fix constraint and EMT calculator
slab.set_constraint(FixAtoms(tags=[0]))
slab.calc = EMT()

# Save initial fixed coordinates
initial_fixed = [a.pos.copy() for a in slab if a.tag == 0]

# Run BFGS optimization
BFGS(slab).run(fmax=0.01)

# Get final fixed coordinates
final_fixed = [a.pos.copy() for a in slab if a.tag == 0]

# Print comparison
print("Initial fixed coords:")
for p in initial_fixed: print(p)
print("\nFinal fixed coords:")
for p in final_fixed: print(p)
print("\nFixed atoms unchanged:", np.allclose(initial_fixed, final_fixed))
