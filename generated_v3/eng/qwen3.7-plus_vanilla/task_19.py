from ase import Atoms
from ase.calculators.lj import LennardJones

atoms = Atoms('CO2', positions=[(-1.16, 0, 0), (0, 0, 0), (1.16, 0, 0)], cell=[10, 10, 10], pbc=False)
atoms.calc = LennardJones()
print(atoms.get_distances([0, 0, 1], [1, 2, 2]))
