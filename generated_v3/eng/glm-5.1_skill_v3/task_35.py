from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

initial = Atoms('Al3', positions=[[0, 0, 0], [1.5, 0, 0], [5, 0, 0]], cell=[10, 10, 10])
final = Atoms('Al3', positions=[[0, 0, 0], [3.5, 0, 0], [5, 0, 0]], cell=[10, 10, 10])

c = FixAtoms(indices=[0, 2])
initial.set_constraint(c)
final.set_constraint(c)

initial.calc = EMT()
final.calc = EMT()

images = [initial] + [initial.copy() for _ in range(3)] + [final]

neb = NEB(images)
neb.interpolate()

for img in images[1:-1]:
    img.calc = EMT()

BFGS(neb).run(fmax=0.05)

for i, img in enumerate(images):
    print(f"Image {i}: {img.get_potential_energy():.4f} eV")
