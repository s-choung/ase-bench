from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create FCC Au bulk structure
atoms = bulk('Au', 'fcc', a=4.08, cubic=True)

# Set EMT calculator
atoms.calc = EMT()

# Use LBFGS optimizer with fmax=0.01
opt = LBFGS(atoms, logfile=None)
opt.run(fmax=0.01)

# Output number of steps and final energy
print(f"Number of optimization steps: {opt.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
