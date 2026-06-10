```python
from ase import Atoms
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB, interpolate

initial = Atoms('Al3', positions=[[0,0,0], [3,0,0], [0.5,0,0]], calculator=EMT())
final = Atoms('Al3', positions=[[0,0,0], [3,0,0], [2.5,0,0]], calculator=EMT())
initial.set_constraint(FixAtoms([0,1]))
final.set_constraint(FixAtoms([0,1]))

images = [initial, final]
interpolate(images, 1)
neb = NEB(images)
BFGS(neb).run(fmax=0.05)

for i, img in enumerate(images):
    print(f"Image {i} energy: {img.get_potential_energy():.4f} eV")
