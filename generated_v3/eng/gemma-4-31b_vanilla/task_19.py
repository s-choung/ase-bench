from ase import Atoms
from ase.calculators.emt import EMT

atoms = Atoms('CO2', 
              positions=[(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)])
atoms.set_cell([10, 10, 10])
atoms.set_pbc(False)
atoms.set_calculator(EMT())

dist = atoms.get_distances(0, slice(1))
print(dist)
