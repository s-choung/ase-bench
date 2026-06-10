from ase import Atoms
from ase.neb import NEB
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

initial = Atoms('Al3', positions=[(0, 0, 0), (3.0, 0, 0), (1.0, 2.0, 0)])
final   = Atoms('Al3', positions=[(0, 0, 0), (3.0, 0, 0), (2.0, 2.0, 0)])

images = [initial.copy()]
images.append(initial.copy())
images.append(final.copy())

constraint = FixAtoms(indices=[0, 1])
for image in images:
    image.set_constraint(constraint)

neb = NEB(images)
neb.interpolate()

for image in images:
    image.calc = EMT()

optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

for i, image in enumerate(images):
    print(f"Image {i}: Energy = {image.get_potential_energy():.6f} eV")
