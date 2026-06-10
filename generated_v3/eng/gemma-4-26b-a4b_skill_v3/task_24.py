from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.filters import FrechetCellFilter

# Build Au FCC bulk and set calculator
atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

# Use FrechetCellFilter to optimize both cell and atomic positions
opt = LBFGS(FrechetCellFilter(atoms))

# Run optimization
# Using a callback to count steps as LBFGS doesn't return it directly
steps = 0
def callback():
    global steps
    steps += 1

opt.run(fmax=0.01, steps=100, callback=callback)

# Output results
print(f"Optimization steps: {steps}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
