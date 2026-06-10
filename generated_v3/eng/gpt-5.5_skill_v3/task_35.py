from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

cell = [10.0, 10.0, 10.0]
fixed = [(2.5, 5.0, 5.0), (7.5, 5.0, 5.0)]

initial = Atoms("Al3", positions=fixed + [(5.0, 3.5, 5.0)], cell=cell, pbc=False)
final = Atoms("Al3", positions=fixed + [(5.0, 6.5, 5.0)], cell=cell, pbc=False)

constraint = FixAtoms(indices=[0, 1])
initial.set_constraint(constraint)
final.set_constraint(constraint)

images = [initial, initial.copy(), final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method="linear")

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05, steps=100)

for i, img in enumerate(images):
    print(f"Image {i}: {img.get_potential_energy():.6f} eV")
