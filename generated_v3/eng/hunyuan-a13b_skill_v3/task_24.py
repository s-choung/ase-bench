from ase import Atoms
from ase.calculators import EMT
from ase.optimize import LBFGS

# Define Au FCC bulk structure
atoms = Atoms('Au', cell='fcc', a=4.08, pbc=True)
atoms.calc = EMT()

# Set up LBFGS optimizer
opt = LBFGS(atoms, trajectory='opt.traj')
steps, final_energy = opt.run(fmax=0.01)

# Print results
print(f"Number of optimization steps: {steps}")
print(f"Final energy (eV): {final_energy}")
