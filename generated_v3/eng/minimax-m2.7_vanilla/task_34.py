import numpy as np
from ase import Atom
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.neb import NEB, idpp_interpolate
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Build Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)

# Top layer z-coordinate
top_z = slab.positions[:, 2].max()

# In‑plane lattice vectors
v1 = slab.cell[0]
v2 = slab.cell[1]

# Fractional positions of fcc and hcp hollow sites
fcc_frac = np.array([1/3, 2/3])
hcp_frac = np.array([2/3, 1/3])

# Height of adatom above surface
height = 2.0

# Cartesian positions for the adatom
pos_fcc = fcc_frac[0] * v1 + fcc_frac[1] * v2 + np.array([0, 0, top_z + height])
pos_hcp = hcp_frac[0] * v1 + hcp_frac[1] * v2 + np.array([0, 0, top_z + height])

# Initial (fcc) and final (hcp) states
initial = slab.copy()
initial.append(Atom('Cu', position=pos_fcc))

final = slab.copy()
final.append(Atom('Cu', position=pos_hcp))

# Create image list (5 images total)
nimages = 5
images = [initial] + [initial.copy() for _ in range(nimages - 2)] + [final]

# Set calculator and constraints for each image
for i, img in enumerate(images):
    img.set_calculator(EMT())
    if i == 0 or i == len(images) - 1:
        # Fix all atoms in the endpoints
        img.set_constraint(FixAtoms(indices=list(range(len(img)))))
    else:
        # Fix substrate, keep adatom free
        img.set_constraint(FixAtoms(indices=list(range(len(img) - 1))))

# IDPP interpolation
idpp_interpolate(images)

# Set up NEB
neb = NEB(images, k=0.1)

# Optimize the band
opt = BFGS(neb)
opt.run(fmax=0.05)

# Compute energies and barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
