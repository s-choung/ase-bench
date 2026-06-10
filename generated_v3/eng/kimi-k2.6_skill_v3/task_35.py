from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import FIRE

initial = Atoms('Al3', positions=[[0.0, 0.0, 0.0], [1.0, 1.5, 0.0], [4.0, 0.0, 0.0]], cell=[10, 10, 10])
final = Atoms('Al3', positions=[[0.0, 0.0, 0.0], [3.0, 1.5, 0.0], [4.0, 0.0, 0.0]], cell=[10, 10, 10])

c = FixAtoms(indices=[0, 2])
initial.set_constraint(c)
final.set_constraint(c)

images = [initial] + [initial.copy() for _ in range(3)] + [final]

for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='linear')

FIRE(neb).run(fmax=0.05)

for i, img in enumerate(images):
    print(i, img.get_potential_energy())
