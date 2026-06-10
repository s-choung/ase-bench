from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
from ase.io import write
import numpy as np

a = 4.05
cell = [10, 10, 10]

initial = Atoms('Al3', positions=[
    [3.0, 5.0, 5.0],
    [7.0, 5.0, 5.0],
    [3.0, 5.0, 7.0],
], cell=cell, pbc=False)

final = Atoms('Al3', positions=[
    [3.0, 5.0, 5.0],
    [7.0, 5.0, 5.0],
    [7.0, 5.0, 7.0],
], cell=cell, pbc=False)

initial.calc = EMT()
final.calc = EMT()

images = [initial]
for _ in range(3):
    img = initial.copy()
    img.calc = EMT()
    images.append(img)
images.append(final)

neb = NEB(images)
neb.interpolate()

for i, img in enumerate(images):
    img.calc = EMT()
    print(f"Image {i}: E = {img.get_potential_energy():.6f} eV")
