from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import build
from ase.neb import NEB
from ase.optimize import BFGS

a = 3.5
initial = Atoms('Al', positions=[(0, 0, 0), (0, 0, 1.5)])
initial.calc = EMT()
final = Atoms('Al', positions=[(0, 0, 0), (0, 0, -1.5)])
final.calc = EMT()

images = [initial.copy(), initial.copy(), final.copy()]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate()
dyn = BFGS(neb, trajectory='neb.traj')
dyn.run(fmax=0.05)

for i, img in enumerate(images):
    print(f"Image {i}: Energy = {img.get_potential_energy()}")
