from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import FrechetCellFilter
from ase.optimize import BFGS

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

# Initial state
print("Initial lattice constant:", atoms.get_cell()[0,0])
print("Initial energy:", atoms.get_potential_energy())

# Optimize with FrechetCellFilter and BFGS
filter = FrechetCellFilter(atoms)
opt = BFGS(filter)
opt.run(fmax=0.01)

# Final state
print("Optimized lattice constant:", atoms.get_cell()[0,0])
print("Optimized energy:", atoms.get_potential_energy())
