from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB

initial = Atoms(
    'Al3',
    positions=[(0.0, 0.0, 0.0), (2.86, 0.0, 0.0), (0.7, 0.0, 0.0)],
    pbc=False,
)
final = Atoms(
    'Al3',
    positions=[(0.0, 0.0, 0.0), (2.86, 0.0, 0.0), (2.16, 0.0, 0.0)],
    pbc=False,
)

constraint = FixAtoms(indices=[0, 1])
initial.set_constraint(constraint)
final.set_constraint(constraint)

images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate()

for img in images:
    img.calc = EMT()

for i, img in enumerate(images):
    e = img.get_potential_energy()
    print(f'Image {i}: E = {e:.6f} eV')
