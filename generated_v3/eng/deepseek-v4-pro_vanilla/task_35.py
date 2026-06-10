from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS

initial = Atoms('Al3', positions=[(0,0,0), (4,0,0), (0.5,0,0)])
initial.set_constraint(FixAtoms(indices=[0, 1]))
initial.calc = EMT()

final = Atoms('Al3', positions=[(0,0,0), (4,0,0), (3.5,0,0)])
final.set_constraint(FixAtoms(indices=[0, 1]))
final.calc = EMT()

mid = initial.copy()
mid.positions[2] = (initial.positions[2] + final.positions[2]) / 2
mid.set_constraint(FixAtoms(indices=[0, 1]))
mid.calc = EMT()

images = [initial, mid, final]
neb = NEB(images)

opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

for i, image in enumerate(neb.images):
    print(f'Image {i} energy: {image.get_potential_energy():.3f} eV')
