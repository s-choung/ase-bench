from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
import numpy as np

# Fixed Al atoms at (0,0,0) and (2,0,0), moving atom at (0.5,0,0) -> (1.5,0,0)
initial = Atoms('Al3', positions=[[0,0,0],[2,0,0],[0.5,0,0]])
final   = Atoms('Al3', positions=[[0,0,0],[2,0,0],[1.5,0,0]])

for atoms in (initial, final):
    atoms.calc = EMT()

# 3 images: initial, one interpolated, final
images = [initial.copy()]
for i in range(1,2):
    pos = initial.get_positions()*(1-i/2) + final.get_positions()*i/2
    img = Atoms('Al3', positions=pos)
    img.calc = EMT()
    images.append(img)
images.append(final.copy())

neb = NEB(images, climb=True)
neb.interpolate()

# Optimize NEB path (max 20 steps for speed)
opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05, steps=20)

# Print energies
for i, img in enumerate(images):
    print(f'Image {i}: Energy = {img.get_potential_energy():.6f} eV')
