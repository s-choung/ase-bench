from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB

initial = Atoms('Al3', positions=[[0, 0, 0], [5, 0, 0], [1, 0, 0]])
final = Atoms('Al3', positions=[[0, 0, 0], [5, 0, 0], [4, 0, 0]])

images = [initial.copy(), initial.copy(), final.copy()]
for atoms in images:
    atoms.set_constraint(FixAtoms(indices=[0, 1]))
    atoms.calc = EMT()

NEB(images).interpolate()
for i, atoms in enumerate(images):
    print(atoms.get_potential_energy())
