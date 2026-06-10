from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

z_vals = sorted(set(a.z for a in slab))
for a in slab:
    a.tag = 0 if a.z <= z_vals[1] else 1

slab.set_constraint(FixAtoms(mask=[a.tag == 0 for a in slab]))

fixed_idx = [a.index for a in slab if a.tag == 0]
before = {i: slab[i].position.copy() for i in fixed_idx}

slab.calc = EMT()
BFGS(slab, logfile=None).run(fmax=0.05)

after = {i: slab[i].position.copy() for i in fixed_idx}

print("Fixed atom indices:", fixed_idx)
for idx in fixed_idx:
    d = np.abs(before[idx] - after[idx]).max()
    print(f"  idx={idx}: before={before[idx]}, after={after[idx]}, max_diff={d:.2e}")
print("All fixed atoms unchanged:", all(np.allclose(before[i], after[i]) for i in fixed_idx))
