from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS
initial = Atoms('Al3', positions=[[0,0,0],[1.5,0,0],[4,0,0]], pbc=False)
final = Atoms('Al3', positions=[[0,0,0],[2.5,0,0],[4,0,0]], pbc=False)
initial.set_constraint(FixAtoms(indices=[0,2]))
final.set_constraint(FixAtoms(indices=[0,2]))
images = [initial] + [initial.copy() for _ in range(1)] + [final]
for img in images[1:-1]:
    img.calc = EMT()
neb = NEB(images, climb=False)
neb.interpolate(method='linear')
for img in images:
    img.calc = EMT()
    print(img.get_potential_energy())
