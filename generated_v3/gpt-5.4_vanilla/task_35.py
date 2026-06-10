from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

initial = Atoms('Al3', positions=[(0, 0, 0), (4.0, 0, 0), (1.0, 0, 0)])
final = Atoms('Al3', positions=[(0, 0, 0), (4.0, 0, 0), (3.0, 0, 0)])

images = [initial]
for _ in range(3):
    img = initial.copy()
    img.calc = EMT()
    images.append(img)
images.append(final)

initial.calc = EMT()
final.calc = EMT()

neb = NEB(images)
neb.interpolate()

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05)

for i, img in enumerate(images):
    print(f'image {i}: {img.get_potential_energy():.6f} eV')
