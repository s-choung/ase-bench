from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = Atoms('H2O', positions=[[0, 0, 0], [0.9, 0, 0], [-0.3, 0.8, 0]])
atoms.calc = EMT()

print(f'Energy before optimization: {atoms.get_potential_energy():.6f} eV')
BFGS(atoms).run(fmax=0.05)
print(f'Energy after optimization:  {atoms.get_potential_energy():.6f} eV')
