import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

cell = [10.0, 10.0, 10.0]
p0 = [3.0, 5.0, 5.0]
p1 = [7.0, 5.0, 5.0]
pmid_i = [4.0, 5.0, 5.0]
pmid_f = [6.0, 5.0, 5.0]

initial = Atoms('Al3', positions=[p0, p1, pmid_i], cell=cell, pbc=False)
final = Atoms('Al3', positions=[p0, p1, pmid_f], cell=cell, pbc=False)

images = [initial] + [initial.copy()] + [final]
neb = NEB(images)
neb.interpolate()

for img in images:
    img.calc = EMT()

for i, img in enumerate(images):
    print(i, img.get_potential_energy())

BFGS(neb).run(fmax=0.05)
for i, img in enumerate(images):
    print(i, img.get_potential_energy())
