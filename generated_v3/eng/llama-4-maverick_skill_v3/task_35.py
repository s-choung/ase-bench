from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

initial = Atoms('Al3', positions=[(0, 0, 0), (3, 0, 0), (1.5, 0, 1)])
final = Atoms('Al3', positions=[(0, 0, 0), (3, 0, 0), (1.5, 0, -1)])
initial.set_constraint([FixAtoms(indices=[0, 1])])
final.set_constraint([FixAtoms(indices=[0, 1])])

images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images, parallel=False)
neb.interpolate()

for img in images:
    img.calc = EMT()
    print(img.get_potential_energy())

opt = BFGS(neb)
opt.run(fmax=0.05)

for img in images:
    print(img.get_potential_energy())
