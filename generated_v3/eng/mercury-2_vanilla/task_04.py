from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build H2O molecule
atoms = molecule('H2O')
atoms.set_calculator(EMT())

# Energy before optimization
e_initial = atoms.get_potential_energy()
print(f'Initial energy: {e_initial:.6f} eV')

# Optimize geometry
dyn = BFGS(atoms)
dyn.run(fmax=0.01)

# Energy after optimization
e_final = atoms.get_potential_energy()
print(f'Final energy: {e_final:.6f} eV')
