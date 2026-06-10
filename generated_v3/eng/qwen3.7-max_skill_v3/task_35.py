from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms

initial = Atoms('Al3', [[0, 0, 0], [4, 0, 0], [2, 2, 0]], cell=[10, 10, 10], pbc=True)
final = Atoms('Al3', [[0, 0, 0], [4, 0, 0], [2, -2, 0]], cell=[10, 10, 10], pbc=True)

images = [initial] + [initial.copy() for _ in range(3)] + [final]

for img in images:
    img.calc = EMT()
    img.set_constraint(FixAtoms(indices=[0, 1]))

neb = NEB(images)
neb.interpolate()

BFGS(neb).run(fmax=0.05)

for i, img in enumerate(images):
    print(f"Image {i} energy: {img.get_potential_energy():.4f} eV")
