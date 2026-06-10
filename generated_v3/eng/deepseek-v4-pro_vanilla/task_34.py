from ase import Atoms, Atom
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB, IDPP
from ase.optimize import BFGS
import numpy as np

# Cu lattice constant
a = 3.61

# Create a FCC(111) slab: (1x1) surface cell, 3 layers, 10 Å vacuum
slab = fcc111('Cu', size=(1, 1, 3), vacuum=10.0, a=a)

# Positions of the three layers
bottom = slab[0]   # tag 0 -> A layer
middle = slab[1]   # tag 1 -> B layer
top    = slab[2]   # tag 2 -> C layer

# In-plane hollow sites
fcc_hollow_xy = bottom.position[:2]   # fcc hollow above A layer
hcp_hollow_xy = middle.position[:2]   # hcp hollow above B layer

# Adatom height: one interlayer spacing above the top layer
d111 = a / np.sqrt(3)
z_adatom = top.position[2] + d111

# Build start (adatom at fcc hollow) and end (adatom at hcp hollow)
start = slab.copy()
start.append(Atom('Cu', (fcc_hollow_xy[0], fcc_hollow_xy[1], z_adatom)))

end = slab.copy()
end.append(Atom('Cu', (hcp_hollow_xy[0], hcp_hollow_xy[1], z_adatom)))

# Fix all substrate atoms (the original slab atoms)
n_slab = len(slab)
mask = [True] * n_slab + [False]   # last atom (adatom) is free
start.set_constraint(FixAtoms(mask=mask))
end.set_constraint(FixAtoms(mask=mask))

# Create 5 images total (start + 3 intermediates + end)
images = [start]
for _ in range(3):
    img = start.copy()
    img.set_constraint(FixAtoms(mask=mask))
    images.append(img)
images.append(end)

# IDPP interpolation to get a reasonable initial path
IDPP(images)

# Assign EMT calculator to all images
for image in images:
    image.calc = EMT()

# NEB optimization (climbing image not necessary for a simple barrier)
neb = NEB(images)
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# Evaluate barrier
energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
