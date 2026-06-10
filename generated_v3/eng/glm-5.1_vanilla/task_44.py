import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

atoms = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# fcc111 automatically tags atoms by layer index (0 to 3)
mask = atoms.get_tags() < 2
atoms.set_constraint(FixAtoms(mask=mask))

init_pos = atoms.get_positions().copy()

atoms.calc = EMT()
opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.05)

final_pos = atoms.get_positions()

print("Fixed atoms coordinates comparison (Before -> After):")
for i in np.where(mask)[0]:
    print(f"Atom {i}: {init_pos[i]} -> {final_pos[i]}")
