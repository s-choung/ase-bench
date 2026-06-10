from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
atoms = molecule('H2O')
atoms.calc = EMT()

# Initial energy
e_initial = atoms.get_potential_energy()
print(f"Initial energy: {e_initial:.6f} eV")

# Optimize
opt = BFGS(atoms, trajectory='h2o_opt.traj')
opt.run(fmax=0.05)

# Final energy
e_final = atoms.get_potential_energy()
print(f"Final energy:   {e_final:.6f} eV")
