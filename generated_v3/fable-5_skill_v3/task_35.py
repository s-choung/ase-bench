from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.constraints import FixAtoms

initial = Atoms('Al3', positions=[[0, 0, 0], [6, 0, 0], [1.5, 2.0, 0]],
                cell=[10, 10, 10])
final = Atoms('Al3', positions=[[0, 0, 0], [6, 0, 0], [4.5, 2.0, 0]],
              cell=[10, 10, 10])

for ends in (initial, final):
    ends.calc = EMT()
    ends.set_constraint(FixAtoms(indices=[0, 1]))
    BFGS(ends, logfile=None).run(fmax=0.02)

images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate()

for img in images[1:-1]:
    img.calc = EMT()
    img.set_constraint(FixAtoms(indices=[0, 1]))

BFGS(neb, logfile=None).run(fmax=0.05)

for i, img in enumerate(images):
    print(f'Image {i}: E = {img.get_potential_energy():.4f} eV')
