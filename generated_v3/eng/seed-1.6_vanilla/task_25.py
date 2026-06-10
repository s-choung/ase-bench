from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FrechetCellFilter

# Cu FCC bulk
atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()

# Initial state
print('Initial cell size:', atoms.get_cell().lengths())
print('Initial energy:', atoms.get_potential_energy())

# Relax cell and positions
fcf = FrechetCellFilter(atoms)
BFGS(fcf).run(fmax=0.01)

# Final state
print('Final cell size:', atoms.get_cell().lengths())
print('Final energy:', atoms.get_potential_energy())
