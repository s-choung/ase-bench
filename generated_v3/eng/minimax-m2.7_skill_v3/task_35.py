from ase import Atoms
from ase.optimize import BFGS
from ase.mep import NEB
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

initial = Atoms('AlAlAl', positions=[(-3, 0, 0), (-1, 0, 0), (3, 0, 0)])
final = Atoms('AlAlAl', positions=[(-3, 0, 0), (1, 0, 0), (3, 0, 0)])

images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate()
BFGS(neb).run(fmax=0.05)

print("\nEnergies:")
for i, img in enumerate(images):
    print(f"  Image {i}: {img.get_potential_energy():.4f} eV")
