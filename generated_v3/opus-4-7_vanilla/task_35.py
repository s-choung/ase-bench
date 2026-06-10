from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

initial = Atoms('Al3', positions=[[0,0,0],[4,0,0],[1,1.5,0]], cell=[8,8,8], pbc=True)
final = Atoms('Al3', positions=[[0,0,0],[4,0,0],[3,1.5,0]], cell=[8,8,8], pbc=True)

initial.calc = EMT()
final.calc = EMT()
BFGS(initial).run(fmax=0.05)
BFGS(final).run(fmax=0.05)

images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images[1:-1]:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate()

opt = BFGS(neb)
opt.run(fmax=0.1, steps=50)

for i, img in enumerate(images):
    print(f"Image {i}: E = {img.get_potential_energy():.4f} eV")
