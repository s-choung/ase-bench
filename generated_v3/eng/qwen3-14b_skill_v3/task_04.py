from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()
print(f'Initial energy: {atoms.get_potential_energy()} eV')
BFGS(atoms).run(fmax=0.05)
print(f'Final energy: {atoms.get_potential_energy()} eV')
