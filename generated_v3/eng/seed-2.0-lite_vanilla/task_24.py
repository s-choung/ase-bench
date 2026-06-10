from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Initialize FCC gold bulk structure
atoms = bulk('Au', 'fcc')
atoms.calc = EMT()

# Run LBFGS geometry optimization
optimizer = LBFGS(atoms)
optimizer.run(fmax=0.01)

# Output requested metrics
print(f"Number of optimization steps: {optimizer.get_number_of_steps()}")
print(f"Final total energy: {atoms.get_potential_energy():.4f} eV")
