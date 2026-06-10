from ase import Atoms
from ase.lattice.surface import fcc111
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
from ase.io import read, write
import numpy as np

# Create Cu (111) slab with 3 layers and 4x4 supercell
slab = fcc111('Cu', size=(4, 4, 3), vacuum=10.0)

# Add a Cu adatom at hollow site (top of layer 4, centered position)
hollow_pos = np.array([0.0, 0.0, 3.0])  # approximate hollow position
slab.append('Cu')
slab.positions[-1] = hollow_pos

# Set calculator
slab.set_calculator(EMT())

# Optimize initial state
bfgs = BFGS(slab)
bfgs.run(fmax=0.05)

# Get initial energy and positions
E_initial = slab.get_potential_energy()
initial_positions = slab.positions.copy()

# Create final state with adatom at hcp site (shifted by 1/3, 1/3 in x,y)
slab2 = slab.copy()
slab2.positions[-1] += np.array([1.0, 1.0, 0.0]) * (1.0/3.0) * slab.get_cell()[0, 0]
bfgs2 = BFGS(slab2)
bfgs2.run(fmax=0.05)
E_final = slab2.get_potential_energy()

# Create 5 images for NEB (including 0 and 6 as endpoints)
images = [slab.copy()]
for i in range(4):
    images.append(slab.copy())
images.append(slab2.copy())

# Interpolate positions using IDPP
neb = NEB(images, parallel=True)
neb.interpolate(idpp=True)

# Set calculator for all images
for image in images:
    image.set_calculator(EMT())

# Optimize NEB path
qn = BFGS(neb, trajectory='neb_opt.traj')
qn.run(fmax=0.05)

# Get maximum energy and barrier
energies = [image.get_potential_energy() for image in images]
E_max = max(energies)
barrier = E_max - E_initial

print(f"Initial energy: {E_initial:.3f} eV")
print(f"Final energy: {E_final:.3f} eV")
print(f"Maximum energy: {E_max:.3f} eV")
print(f"Diffusion barrier: {barrier:.3f} eV")
