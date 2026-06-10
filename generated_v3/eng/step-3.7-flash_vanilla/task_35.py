from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS

initial = Atoms('Al3', positions=[[0, 0, 0], [6.0, 0, 0], [1.0, 0, 0]])
final = initial.copy()
final.positions[2] = [5.0, 0, 0]
images = [initial, initial.copy(), final]

for img in images:
    img.calc = EMT()
    img.set_constraint(FixAtoms(mask=[True, True, False]))

neb = NEB(images)
neb.interpolate()
BFGS(neb).run(fmax=0.01)

for i, img in enumerate(images):
    print(f"Image {i} energy: {img.get_potential_energy():.3f} eV")
