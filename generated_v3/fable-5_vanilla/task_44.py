from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
mask = [atom.tag >= 3 for atom in slab]  # tag 1=top layer, 4=bottom layer
slab.set_constraint(FixAtoms(mask=mask))
slab.calc = EMT()

pos_before = slab.get_positions().copy()
opt = BFGS(slab, logfile='-')
opt.run(fmax=0.01)
pos_after = slab.get_positions()

print("\nFixed atoms position comparison:")
for i, atom in enumerate(slab):
    if mask[i]:
        diff = np.linalg.norm(pos_after[i] - pos_before[i])
        print(f"atom {i} (tag={atom.tag}): before={pos_before[i]}, after={pos_after[i]}, |diff|={diff:.2e}")

print("\nAll fixed atoms unchanged:", np.allclose(pos_before[mask], pos_after[mask]))
