from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Setup Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print(f"Before: Cell = {atoms.get_cell().lengths()}, Energy = {atoms.get_potential_energy():.4f} eV")

# Simultaneous optimization of cell and positions
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print(f"After:  Cell = {atoms.get_cell().lengths()}, Energy = {atoms.get_potential_energy():.4f} eV")
