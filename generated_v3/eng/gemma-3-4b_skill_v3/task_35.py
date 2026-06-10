from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.spacegroup import crystal
from ase.build import bulk
import numpy as np

# Create the initial and final states
initial = bulk('Al', 'fcc', a=3.6, cubic=True, orthorhombic=True)
initial.set_cell(initial.get_cell())
initial.positions[:, 2] = 3.6
initial.calc = EMT()

final = bulk('Al', 'fcc', a=3.6, cubic=True, orthorhombic=True)
final.set_cell(final.get_cell())
final.positions[:, 2] = 1.0
final.calc = EMT()


# Create the NEB object
images = [initial] + [initial.copy() for _ in range(2)] + [final]
neb = NEB(images, interpolation='idpp')
neb.interpolate(method='idpp')

# Perform the NEB calculation
for img in images[1:-1]:
    img.calc = EMT()

neb.run(fmax=0.05)

# Print the energy of each image
for i, img in enumerate(images):
    print(f"Image {i}: Energy = {img.get_potential_energy():.4f} eV")
