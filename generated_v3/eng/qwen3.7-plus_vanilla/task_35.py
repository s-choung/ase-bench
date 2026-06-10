from ase import Atoms
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import FIRE

initial = Atoms('Al3', positions=[(0, 0, 0), (4.05, 0, 0), (0.5, 0, 0)])
final = Atoms('Al3', positions=[(0, 0, 0), (4.05, 0, 0), (3.55, 0, 0)])

mask = [True, True, False]
initial.set_constraint(FixAtoms(mask=mask))
final.set_constraint(FixAtoms(mask=mask))

images = [initial.copy(), initial.copy(), final.copy()]
for i in range(3):
    pos = initial.get_positions() + (i / 2.0) * (final.get_positions() - initial.get_positions())
    images[i].set_positions(pos)
    images[i].calc = EMT()

neb = NEB(images, climb=True)
dyn = FIRE(neb)
dyn.run(fmax=0.05)

for i, img in enumerate(images):
    print(f"Image {i} energy: {img.get_potential_energy():.4f} eV")
