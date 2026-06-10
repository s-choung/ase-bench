from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms

initial = Atoms('Al3',
    [[0.0, 0.0, 0.0], [2.9, 0.0, 0.0], [-2.0, 2.0, 0.0]],
    cell=[12, 12, 12], pbc=False, constraint=FixAtoms(indices=[0, 1]))

final = Atoms('Al3',
    [[0.0, 0.0, 0.0], [2.9, 0.0, 0.0], [4.9, 2.0, 0.0]],
    cell=[12, 12, 12], pbc=False, constraint=FixAtoms(indices=[0, 1]))

initial.calc = EMT()
final.calc = EMT()

images = [initial] + [initial.copy()] + [final]
for i in range(len(initial)):
    images[1].positions[i] = 0.5 * (initial.positions[i] + final.positions[i])
images[1].calc = EMT()

neb = NEB(images)
opt = BFGS(neb)
opt.run(fmax=0.05)

for i, img in enumerate(images):
    print(f'Image {i}: E = {img.get_potential_energy():.4f} eV')
