from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Initial and final states: third Al atom moves between two fixed Al atoms
initial = Atoms('Al3', positions=[(0, 0, 0), (2.8, 0, 0), (1.4, 1.5, 0)])
final   = Atoms('Al3', positions=[(0, 0, 0), (2.8, 0, 0), (1.4, -1.5, 0)])

for a in (initial, final):
    a.calc = EMT()

images = [initial, initial.copy(), final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate()

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05, steps=20)

for i, img in enumerate(images):
    print(f"Image {i}: energy = {img.get_potential_energy():.6f} eV")
