from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep.neb import NEB
from ase.optimize import BFGS

c = FixAtoms(indices=[0, 2])
initial = Atoms('Al3', positions=[(0, 0, 0), (1.0, 0, 0), (4.0, 0, 0)], constraints=c)
final = Atoms('Al3', positions=[(0, 0, 0), (3.0, 0, 0), (4.0, 0, 0)], constraints=c)

images = [initial] + [initial.copy() for _ in range(3)] + [final]

neb = NEB(images)
neb.interpolate()

for img in images:
    img.calc = EMT()

opt = BFGS(neb)
opt.run(fmax=0.05)

for i, img in enumerate(images):
    print(f"Image {i}: {img.get_potential_energy():.4f} eV")
