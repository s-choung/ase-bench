from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

initial = Atoms("Al3", positions=[(0, 0, 0), (5, 0, 0), (1.5, 0, 0)])
final = Atoms("Al3", positions=[(0, 0, 0), (5, 0, 0), (3.5, 0, 0)])

constraint = FixAtoms(indices=[0, 1])
initial.set_constraint(constraint)
final.set_constraint(constraint)

images = [initial]
for _ in range(3):
    img = initial.copy()
    img.set_constraint(constraint)
    images.append(img)
images.append(final)

for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate()

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05, steps=100)

for i, img in enumerate(images):
    print(i, img.get_potential_energy())
