from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

atoms_i = Atoms('Al3', positions=[(0.0, 0.0, 0.0), (4.0, 0.0, 0.0), (1.0, 0.0, 0.0)])
atoms_f = Atoms('Al3', positions=[(0.0, 0.0, 0.0), (4.0, 0.0, 0.0), (3.0, 0.0, 0.0)])

images = [atoms_i, atoms_i.copy(), atoms_f]

for img in images:
    img.calc = EMT()
    img.set_constraint(FixAtoms(indices=[0, 1]))

neb = NEB(images)
neb.interpolate()

BFGS(neb).run(fmax=0.05)

for i, img in enumerate(images):
    print(f"Image {i} energy: {img.get_potential_energy():.4f} eV")
