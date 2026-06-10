from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Initialize Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

# Print initial state
print('Initial cell:', atoms.get_cell_lengths_and_angles())
print('Initial energy (eV):', atoms.get_potential_energy())

# Optimize cell + positions
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Print final state
print('Final cell:', atoms.get_cell_lengths_and_angles())
print('Final energy (eV):', atoms.get_potential_energy())
