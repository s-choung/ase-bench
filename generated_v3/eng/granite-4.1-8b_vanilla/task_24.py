from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Define Au FCC bulk structure
a = 4.078  # Gold lattice constant in Ångström
cells = [2, 2, 2]
atoms = Atoms('Au',
              positions=[[0, 0, 0]],
              cell=[a * cells[0], a * cells[1], a * cells[2]],
              pbc=True)

# Assign EMT calculator
atoms.calc = EMT()

# Set up LBFGS optimizer with force tolerance
optimizer = LBFGS(atoms, fmax=0.01)

# Run optimization
trajectory = optimizer.run(maxstep=100)

# Extract optimization steps and final energy
steps = len(trajectory)
final_energy = atoms.get_potential_energy()

print(f'Number of optimization steps: {steps}')
print(f'Final energy: {final_energy:.6f} eV')
