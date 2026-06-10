from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.filters import FrechetCellFilter

# Initialize Au FCC bulk
au_bulk = bulk('Au', 'fcc', a=4.08, cubic=True)
# Assign built-in EMT calculator
au_bulk.calc = EMT()
# Enable simultaneous cell and atomic position optimization
relax_system = FrechetCellFilter(au_bulk)
# Set up LBFGS optimizer
opt = LBFGS(relax_system)
# Run optimization with specified force threshold
opt.run(fmax=0.01)
# Output required metrics
print(f"Optimization steps: {opt.nsteps}")
print(f"Final total energy (eV): {au_bulk.get_potential_energy():.4f}")
