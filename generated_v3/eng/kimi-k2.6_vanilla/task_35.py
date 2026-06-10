from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS

initial = Atoms('Al3', positions=[[0.0, 0.0, 0.0],
                                  [1.5, 0.0, 0.0],
                                  [5.0, 0.0, 0.0]])
initial.set_constraint(FixAtoms(indices=[0, 2]))
initial.calc = EMT()

final = Atoms('Al3', positions=[[0.0, 0.0, 0.0],
                                [3.5, 0.0, 0.0],
                                [5.0, 0.0, 0.0]])
final.set_constraint(FixAtoms(indices=[0, 2]))
final.calc = EMT()

images = [initial] + [initial.copy() for _ in range(3)] + [final]
for image in images[1:4]:
    image.calc = EMT()

neb = NEB(images)
neb.interpolate()

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05)

for i, image in enumerate(images):
    print(i, image.get_potential_energy())
