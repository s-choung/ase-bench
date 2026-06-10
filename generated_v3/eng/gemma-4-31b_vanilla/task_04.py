from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Setup H2O molecule
mol = Atoms('H2O', positions=[[0, 0, 0], [0, 0.7, 0.6], [0, -0.7, 0.6]])
mol.set_calculator(EMT())

# Initial energy
print(f"Initial energy: {mol.get_potential_energy():.4f} eV")

# Optimize geometry
dyn = BFGS(mol)
dyn.run(fmax=0.05)

# Final energy
print(f"Final energy: {mol.get_potential_energy():.4f} eV")
