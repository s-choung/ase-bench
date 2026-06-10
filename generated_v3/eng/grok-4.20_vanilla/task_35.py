from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
import numpy as np

# Initial state: Al atoms at 0 and 2.5 Ang, third at 0.5
initial = Atoms('Al3',
                positions=[[0, 0, 0],
                           [0.5, 0, 0],
                           [2.5, 0, 0]],
                cell=[5, 5, 5],
                pbc=False)
initial.calc = EMT()

# Final state: Al atoms at 0 and 2.5 Ang, third at 2.0
final = Atoms('Al3',
              positions=[[0, 0, 0],
                         [2.0, 0, 0],
                         [2.5, 0, 0]],
              cell=[5, 5, 5],
              pbc=False)
final.calc = EMT()

# Create 3 images with linear interpolation
images = [initial.copy() for _ in range(3)]
images[-1] = final.copy()
neb = NEB(images)
neb.interpolate()

# Attach EMT calculator to images
for img in images:
    img.calc = EMT()

# Print energies of each image
energies = [img.get_potential_energy() for img in images]
for i, e in enumerate(energies):
    print(f'Image {i}: {e:.6f} eV')
