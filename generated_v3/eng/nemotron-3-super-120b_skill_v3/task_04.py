from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
atoms = molecule('H2O')
atoms.calc = EMT()

# Energy before optimization
e_initial = atoms.get_potential_energy()
print(f"Initial energy: {e_initial:.4f} eV")

# Optimize geometry
optimizer = BFGS(atoms)
optimizer.run(fmax=0.05)

# Energy after optimization
e_final = atoms.get_potential_energy()
print(f"Final energy: {e_final:.4f} eV")
