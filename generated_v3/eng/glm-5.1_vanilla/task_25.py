from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.7)
atoms.calc = EMT()

print(f"Before: Cell = {atoms.cell.lengths()}, Energy = {atoms.get_potential_energy():.4f}")

ecf = FrechetCellFilter(atoms)
opt = BFGS(ecf)
opt.run(fmax=0.01)

print(f"After: Cell = {atoms.cell.lengths()}, Energy = {atoms.get_potential_energy():.4f}")
