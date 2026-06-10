from ase import Atoms, optimize
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT

slab = fcc111('Cu', size=(4,4,4), vacuum=10.0)
tags = slab.get_tags()
tags[-8:] = 1  # Fix last two layers (8 atoms each for 4x4)
slab.set_tags(tags)
mask = tags == 1
slab.calc = EMT()

fixed_pos = slab.positions[mask].copy()

opt = optimize.BFGS(slab, trajectory=None)
opt.run(fmax=0.01)

assert np.allclose(slab.positions[mask], fixed_pos), "Fixed atoms moved!"
print("Fixed positions ok. Initial:", fixed_pos, "Final:", slab.positions[mask])
