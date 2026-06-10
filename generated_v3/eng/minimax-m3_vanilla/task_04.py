from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = Atoms('H2O', positions=[[0, 0, 0], [0.96, 0, 0], [-0.24, 0.93, 0]])
atoms.calc = EMT()

e0 = atoms.get_potential_energy()
print(f"Energy before: {e0:.6f} eV")

BFGS(atoms).run()

e1 = atoms.get_potential_energy()
print(f"Energy after:  {e1:.6f} eV")
