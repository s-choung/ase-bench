from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

initial = Atoms(
    "Al3",
    positions=[
        [0.0, 0.0, 0.0],
        [5.0, 0.0, 0.0],
        [2.5, -1.5, 0.0],
    ],
)

final = Atoms(
    "Al3",
    positions=[
        [0.0, 0.0, 0.0],
        [5.0, 0.0, 0.0],
        [2.5, 1.5, 0.0],
    ],
)

constraint = FixAtoms(indices=[0, 1])
initial.set_constraint(constraint)
final.set_constraint(constraint)

images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate(method="linear")

for image in images:
    image.calc = EMT()

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05, steps=100)

for i, image in enumerate(images):
    print(i, image.get_potential_energy())
