from ase.build import fcc_slab
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

atoms = fcc_slab('Cu', a=3.6, layers=4, orientation=[1,1,1])
z = atoms.positions[:,2]
unique_z = np.unique(z)
bot_z = unique_z[:2]

tags = np.zeros(len(atoms), int)
for i, zi in enumerate(z):
    if np.isclose(zi, bot_z[0]) or np.isclose(zi, bot_z[1]):
        tags[i] = 1
atoms.set_tags(tags)
atoms.set_constraint(FixAtoms(mask=tags==1))
atoms.calc = EMT()

fixed = np.where(tags==1)[0]
orig = atoms.positions[fixed]

dyn = BFGS(atoms)
dyn.run(fmax=0.01)

new = atoms.positions[fixed]

for o, n in zip(orig, new):
    print(f"Original: {o}, Optimized: {n}")
