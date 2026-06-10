from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

initial = Atoms(
    'Al3',
    positions=[
        [0.0, 0.0, 0.0],
        [4.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
    ],
    cell=[10.0, 10.0, 10.0],
    pbc=False,
)

final = Atoms(
    'Al3',
    positions=[
        [0.0, 0.0, 0.0],
        [4.0, 0.0, 0.0],
        [3.0, 0.0, 0.0],
    ],
    cell=[10.0, 10.0, 10.0],
    pbc=False,
)

images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate()

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05, steps=200)

for i, img in enumerate(images):
    print(f'image {i}: {img.get_potential_energy():.6f} eV')
