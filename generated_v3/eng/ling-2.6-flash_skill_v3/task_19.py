from ase import Atoms
from ase.calculators.emt import EMT

atoms = Atoms('CO2', positions=[[0, 0, 0], [0, 0, 1.16], [0, 0, -1.16]])
atoms.set_cell([10, 10, 10])
atoms.set_pbc(False)
atoms.calc = EMT()

d = atoms.get_distances(0, [1, 2])
print('C–O distances (Å):', d)
