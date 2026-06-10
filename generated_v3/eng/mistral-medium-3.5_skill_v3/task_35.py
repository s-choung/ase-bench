from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB

initial = Atoms('Al3', positions=[(0, 0, 0), (0, 0, 2.5), (0, 0, 1.0)])
final = Atoms('Al3', positions=[(0, 0, 0), (0, 0, 2.5), (0, 0, 1.5)])
images = [initial] + [initial.copy() for _ in range(1)] + [final]

neb = NEB(images)
neb.interpolate()
for img in images:
    img.calc = EMT()
for img in images:
    print(img.get_potential_energy())
