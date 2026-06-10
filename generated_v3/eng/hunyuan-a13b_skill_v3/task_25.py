from ase import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.eos import EquationOfState

# Create Cu FCC bulk
atoms = bulk("Cu", "fcc", a=3.6, cubic=True)
print("Initial cell:", atoms.cell)
print("Initial energy:", atoms.get_potential_energy())

# Optimize with FrechetCellFilter and BFGS
atoms.calc = EMT()
opt = BFGS(FrechetCellFilter(atoms), fmax=0.01)
opt.run()

# Print optimized cell and energy
print("Optimized cell:", atoms.cell)
print("Optimized energy:", atoms.get_potential_energy())
