"""T7 Wiki: NEB path between two Al configurations"""
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

initial = fcc111('Al', size=(2, 2, 1), vacuum=5.0)
initial.calc = EMT()

final = initial.copy()
final[-1].position[0] += 2.0
final.calc = EMT()

images = [initial]
images += [initial.copy() for _ in range(3)]
images += [final]

neb = NEB(images)
neb.interpolate(method='idpp')

for img in images[1:-1]:
    img.calc = EMT()

optimizer = BFGS(neb)
optimizer.run(fmax=0.1, steps=5)
print("NEB completed successfully")
