from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
initial = Atoms('Al3', positions=[[0,0,0],[3,0,0],[1,0.5,0]], cell=[10,10,10])
final = Atoms('Al3', positions=[[0,0,0],[3,0,0],[2,0.5,0]], cell=[10,10,10])
initial.set_constraint(FixAtoms(indices=[0,1]))
final.set_constraint(FixAtoms(indices=[0,1]))
images = [initial]
for _ in range(1):
    images.append(initial.copy())
images.append(final)
neb = NEB(images, k=0.1)
neb.interpolate()
for img in images:
    img.calc = EMT()
    print(img.get_potential_energy())
