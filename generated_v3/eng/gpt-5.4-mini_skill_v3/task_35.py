from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

initial = Atoms('Al3', positions=[(0, 0, 0), (2.8, 0, 0), (1.4, 1.5, 0)])
final = Atoms('Al3', positions=[(0, 0, 0), (2.8, 0, 0), (1.4, -1.5, 0)])

images = [initial, initial.copy(), final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate()

BFGS(neb).run(fmax=0.05, steps=50)

for i, img in enumerate(images):
    print(i, img.get_potential_energy())
