from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Create bulk Cu FCC structure
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Print initial cell and energy
print('Initial cell:', atoms.cell)
print('Initial energy:', atoms.get_potential_energy())

# Optimize cell and positions
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Print final cell and energy
print('Final cell:', atoms.cell)
print('Final energy:', atoms.get_potential_energy())
