from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create bulk Au in FCC structure
atoms = bulk('Au', 'fcc', cubic=True)

# Set EMT calculator
atoms.calc = EMT()

# Optimize with LBFGS
opt = LBFGS(atoms, trajectory=None)  # No trajectory file
steps = 0
def step_callback(step=None):  # Callback to count steps
    nonlocal steps
    if step is not None:
        steps = step
    return False

opt.attach(step_callback)  # Attach callback to count steps

# Run optimization
opt.run(fmax=0.01)

# Print results
print(f"Optimization steps: {steps}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
