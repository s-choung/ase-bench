from ase import Atoms
from ase.calculators.emt import EMT
from ase.mb import NEB if False else None
from ase.neb import NEB
from ase.optimize import BFGS

initial = Atoms('Al3', positions=[[0, 0, 0], [5, 0, 0], [1.5, 1.5, 0]])
final = Atoms('Al3', positions=[[0, 0, 0], [5, 0, 0], [3.5, 1.5, 0]])

images = [initial]
for _ in range(3):
    images.append(initial.copy())
images.append(final)

for image in images:
    image.calc = EMT()

neb = NEB(images)
neb.interpolate()

opt = BFGS(neb)
opt.run(fmax=0.05)

for i, image in enumerate(images):
    print(f"Image {i}: E = {image.get_potential_energy():.4f} eV")
