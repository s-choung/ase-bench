from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = Atoms('H2O', positions=[[0.96, 0, 0], [-0.24, 0.93, 0], [0, 0, 0]])
atoms.calc = EMT()
print(f"Initial energy: {atoms.get_potential_energy():.4f} eV")
BFGS(atoms).run(fmax=0.01)
print(f"Optimized energy: {atoms.get_potential_energy():.4f} eV")
