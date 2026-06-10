from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.neb import NEB
import numpy as np

# ---------- Build end points ----------
# Fixed Al atoms at 0 Å and 3 Å, moving Al will slide from 1 Å → 2 Å
init = Atoms('Al3', positions=[[0, 0, 0],
                               [3, 0, 0],
                               [1, 0, 0]],
             pbc=False)
final = Atoms('Al3', positions=[[0, 0, 0],
                                [3, 0, 0],
                                [2, 0, 0]],
              pbc=False)

# Freeze the two outer atoms (indices 0,1)
fix = FixAtoms(indices=[0, 1])
init.set_constraint(fix)
final.set_constraint(fix)

# ---------- Prepare NEB images ----------
n_inter = 3                     # number of intermediate images
images = [init] + [init.copy() for _ in range(n_inter)] + [final]

# Attach calculator (EMT) to all images (including ends)
for img in images:
    img.calc = EMT()

# Linear interpolation of the path
neb = NEB(images, climb=False)
neb.interpolate()               # default = linear

# ---------- Relax the band ----------
opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

# ---------- Report energies ----------
print("NEB image energies (eV):")
for i, img in enumerate(images):
    print(f"  image {i:02d}: {img.get_potential_energy():.6f} eV")
