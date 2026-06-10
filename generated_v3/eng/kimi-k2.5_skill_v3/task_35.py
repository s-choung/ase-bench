from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

initial = Atoms('Al3', positions=[[0,0,0],[4,0,0],[1,0,0]])
initial.set_constraint(FixAtoms(indices=[0,1]))
initial.calc = EMT()

final = Atoms('Al3', positions=[[0,0,0],[4,0,0],[3,0,0]])
final.set_constraint(FixAtoms(indices=[0,1]))
final.calc = EMT()

images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images[1:-1]:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='linear')
BFGS(neb).run(fmax=0.05)

for i, img in enumerate(images):
    print(f"Image {i}: {img.get_potential_energy():.4f} eV")
