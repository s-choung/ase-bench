from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.constraints import FixAtoms
from ase.optimize import FIRE

pos_fixed = [(0.0, 0.0, 0.0), (5.0, 0.0, 0.0)]
initial = Atoms('Al3', positions=pos_fixed + [(2.5, 2.0, 0.0)], pbc=False, cell=[10, 10, 10])
final = Atoms('Al3', positions=pos_fixed + [(2.5, -2.0, 0.0)], pbc=False, cell=[10, 10, 10])

calc = EMT()
fix = FixAtoms(indices=[0, 1])

for atoms in [initial, final]:
    atoms.calc = calc
    atoms.set_constraint(fix)

images = [initial]
for _ in range(3):
    img = initial.copy()
    img.calc = calc
    img.set_constraint(fix)
    images.append(img)
images.append(final)

neb = NEB(images)
neb.interpolate()

opt = FIRE(neb)
opt.run(fmax=0.05)

for i, img in enumerate(images):
    print(f"Image {i} Energy: {img.get_potential_energy():.4f} eV")
