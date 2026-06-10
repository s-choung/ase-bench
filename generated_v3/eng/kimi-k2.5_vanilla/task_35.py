from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS

initial = Atoms('AlAlAl', positions=[[0,0,0], [4,0,0], [1,0,0]], cell=[10,10,10], pbc=False)
initial.set_constraint(FixAtoms(indices=[0,1]))
initial.calc = EMT()

final = Atoms('AlAlAl', positions=[[0,0,0], [4,0,0], [3,0,0]], cell=[10,10,10], pbc=False)
final.set_constraint(FixAtoms(indices=[0,1]))
final.calc = EMT()

images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate()

for img in images[1:-1]:
    img.calc = EMT()

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.1)

for i, img in enumerate(images):
    print(f"Image {i}: {img.get_potential_energy():.4f} eV")
