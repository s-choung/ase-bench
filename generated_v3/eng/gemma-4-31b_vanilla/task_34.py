import numpy as np
from ase import Atoms
from ase.build import fcc111_surface
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Setup surface and adatom
slab = fcc111_surface('Cu', size=(3, 3, 3), vacuum=10.0)
slab.calc = EMT()

# Define hollow sites
# FCC hollow is roughly (0.5, 0.5) in fractional coordinates of the surface unit cell
# HCP hollow is roughly (0.5, 0.0) 
# We place the adatom at a fixed height z above the surface
z_height = slab.get_cell()[2][2] * 0.1 + slab.positions[-1, 2]

# Initial state (FCC hollow)
initial = slab.copy()
initial.append(Atoms('Cu', positions=[[0.5, 0.5, z_height]])) 
initial.calc = EMT()

# Final state (HCP hollow)
final = slab.copy()
final.append(Atoms('Cu', positions=[[0.5, 0.0, z_height]]))
final.calc = EMT()

# NEB Setup
n_images = 5
images = [initial.copy() for i in range(n_images)]
for image in images:
    image.calc = EMT()

neb = NEB(images)
neb.interpolate(initial, final, method='idpp')

# Optimization
optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

# Energy Barrier calculation
energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]

print(f"Energy Barrier: {barrier:.4f} eV")
