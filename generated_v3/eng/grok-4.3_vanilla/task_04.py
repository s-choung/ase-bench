from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
atoms = Atoms('H2O', positions=[[0, 0, 0], [0, 0, 1], [0, 1, 0]])
atoms.calc = EMT()
print(atoms.get_potential_energy())
BFGS(atoms).run(fmax=0.05)
print(atoms.get_potential_energy())
