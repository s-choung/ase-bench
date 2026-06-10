from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
import numpy as np

# Initial state: Al atom at origin
initial = Atoms('Al3', positions=[[0, 0, 0], [3, 0, 0], [1.5, 0, 0]])
initial.center(vacuum=5)

# Final state: Al atom moved to other side
final = Atoms('Al3', positions=[[0, 0, 0], [3, 0, 0], [4.5, 0, 0]])
final.center(vacuum=5)

# Create NEB images (3 intermediate images)
images = [initial] + [initial.copy() for _ in range(3)] + [final]

# Linear interpolation
neb = NEB(images)
neb.interpolate(method='linear')

# Set calculator for intermediate images only
for img in images[1:-1]:
    img.calc = EMT()

# Run NEB
dyn = BFGS(neb, trajectory='neb.traj')
dyn.run(fmax=0.1, steps=100)

# Print energies
print("NEB Image Energies:")
for i, img in enumerate(images):
    img.calc = EMT()
    e = img.get_potential_energy()
    print(f"Image {i}: {e:.4f} eV")
