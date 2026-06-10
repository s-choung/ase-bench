from ase import Atom, Atoms
from ase.io import write
from ase.calculators import EMT
from ase.optimize import BFGS

# Create a 4-layer Cu(111) slab
Cu = {1: {"symbol": "Cu", "magmom": 1.0}, 2: {"symbol": "O", "magmom": 0.0}}

size = (5, 5, 4)
slab = Atoms([], cell=size, pbc=True)
for layer in range(1, 5):
    for x in range(size[0]):
        for y in range(size[1]):
            pos = (x + (layer-1)*0.33, y + (layer-1)*0.33, 0)
            tags = [] if layer > 2 else [layer]
            slab += Atom(Cu[layer]["symbol"], pos, magmom=Cu[layer]["magmom"], tags=tags)

# Fix the bottom two layers
slab.get_atoms_with_tag(1).fix()
slab.get_atoms_with_tag(2).fix()

# Initial coordinates
before_opt = slab.positions.copy()

# Setup EMT and BFGS optimization
calc = EMT()
slab.set_calculator(calc)
optim = BFGS(slab)
optim.kernel()

# Final coordinates
after_opt = slab.positions.copy()

# Print before and after fixed atoms
fixed_before = slab.get_atoms_with_tag(1).position
fixed_after = slab.get_atoms_with_tag(1).position
print("Fixed atoms before and after optimization:")
print(fixed_before, fixed_after)
