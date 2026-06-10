from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB

d = 4.0
initial = Atoms('Al3', positions=[[0,0,0], [0,0,d], [0,0,1.0]], cell=[10,10,10], pbc=False)
final = Atoms('Al3', positions=[[0,0,0], [0,0,d], [0,0,d-1.0]], cell=[10,10,10], pbc=False)

images = [initial, initial.copy(), final]
for atoms in images:
    atoms.set_constraint(FixAtoms(indices=[0,1]))
    atoms.calc = EMT()

neb = NEB(images)
neb.interpolate()

for i, atoms in enumerate(images):
    print(f"Image {i}: energy = {atoms.get_potential_energy():.6f} eV")
