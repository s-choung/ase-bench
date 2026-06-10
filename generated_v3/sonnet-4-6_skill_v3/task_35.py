import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB

d = 2.86

initial = Atoms('Al3', positions=[[0, 0, 0], [d*2, 0, 0], [d*0.5, 0, 0]])
initial.cell = [10, 10, 10]
initial.pbc = True

final = Atoms('Al3', positions=[[0, 0, 0], [d*2, 0, 0], [d*1.5, 0, 0]])
final.cell = [10, 10, 10]
final.pbc = True

for atoms in [initial, final]:
    atoms.calc = EMT()
    opt = BFGS(atoms, logfile=None)
    opt.run(fmax=0.05)

images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate()

for img in images[1:-1]:
    img.calc = EMT()

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05)

print("Image energies after NEB:")
for i, img in enumerate(images):
    img.calc = EMT()
    e = img.get_potential_energy()
    print(f"  Image {i}: {e:.4f} eV")
