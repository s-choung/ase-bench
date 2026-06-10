from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FrechetCellFilter

# Create Cu FCC bulk with an initial guess for lattice constant
cu = bulk('Cu', 'fcc', a=3.6)  # Å
cu.calc = EMT()

# Initial cell and energy
print('Initial cell:', cu.get_cell())
print('Initial energy:', cu.get_potential_energy(), 'eV')

# Relax cell shape/volume and atomic positions
fcf = FrechetCellFilter(cu)
opt = BFGS(fcf)
opt.run(fmax=0.01)

# Final cell and energy
print('Optimized cell:', cu.get_cell())
print('Optimized energy:', cu.get_potential_energy(), 'eV')
