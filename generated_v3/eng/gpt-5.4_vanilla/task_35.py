from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Two fixed Al atoms; third Al moves between them
initial = Atoms(
    'Al3',
    positions=[(0.0, 0.0, 0.0),
               (4.0, 0.0, 0.0),
               (1.0, 0.0, 0.0)]
)

final = Atoms(
    'Al3',
    positions=[(0.0, 0.0, 0.0),
               (4.0, 0.0, 0.0),
               (3.0, 0.0, 0.0)]
)

images = [initial.copy() for _ in range(3)]
images[0] = initial.copy()
images[-1] = final.copy()

for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate()

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05, steps=100)

for i, img in enumerate(images):
    print(f'Image {i}: E = {img.get_potential_energy():.6f} eV')
