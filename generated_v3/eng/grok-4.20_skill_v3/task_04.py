from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()
print(atoms.get_potential_energy())
BFGS(atoms).run(fmax=0.01)
print(atoms.get_potential_energy())
