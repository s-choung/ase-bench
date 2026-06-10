from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB

initial = Atoms('Al3', [(0, 0, 0), (4, 0, 0), (2, 2, 0)])
final = Atoms('Al3', [(0, 0, 0), (4, 0, 0), (2, -2, 0)])

initial.calc = EMT()
final.calc = EMT()

images = [initial]
for i in range(3):
    image = initial.copy()
    image.positions[2] = initial.positions[2] + (final.positions[2] - initial.positions[2]) * (i + 1) / 4
    image.calc = EMT()
    images.append(image)
images.append(final)

neb = NEB(images, parallel=False)
neb.interpolate()

for image in images:
    print(image.get_potential_energy())

dyn = BFGS(neb)
dyn.run(fmax=0.05)

for image in images:
    print(image.get_potential_energy())
