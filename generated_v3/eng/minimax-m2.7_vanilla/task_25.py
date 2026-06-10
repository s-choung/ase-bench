from ase.build import bulk
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.calculators.emt import EMT

# Cu FCC bulk with an approximate lattice constant
cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()

# Initial state
E_initial = cu.get_potential_energy()
a_initial = cu.cell[0,0]
print(f"Before optimization: a = {a_initial:.4f} Å, E = {E_initial:.4f} eV")

# Optimize lattice constant and atomic positions
opt = BFGS(FrechetCellFilter(cu))
opt.run(fmax=0.01)

# Optimized state
E_final = cu.get_potential_energy()
a_final = cu.cell[0,0]
print(f"After  optimization: a = {a_final:.4f} Å, E = {E_final:.4f} eV")
