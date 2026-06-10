from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import FIRE

initial = Atoms("Al3", positions=[(0, 0, 0), (4, 0, 0), (1, 0, 0)])
final = Atoms("Al3", positions=[(0, 0, 0), (4, 0, 0), (3, 0, 0)])

constraint = FixAtoms(indices=[0, 1])
initial.set_constraint(constraint)
final.set_constraint(constraint)

images = [initial, initial.copy(), final]
for img in images:
    img.calc = EMT()
    img.set_constraint(constraint)

neb = NEB(images)
neb.interpolate()

opt = FIRE(neb, logfile=None)
opt.run(fmax=0.05, steps=100)

for i, img in enumerate(images):
    print(f"Image {i}: energy = {img.get_potential_energy():.6f} eV")
