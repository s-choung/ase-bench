from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

print(f"Before: a = {atoms.cell.lengths()[0]:.4f} Å, Energy = {atoms.get_potential_energy():.4f} eV")

ecf = FrechetCellFilter(atoms)
opt = BFGS(ecf)
opt.run(fmax=0.01)

print(f"After:  a = {atoms.cell.lengths()[0]:.4f} Å, Energy = {atoms.get_potential_energy():.4f} eV")
