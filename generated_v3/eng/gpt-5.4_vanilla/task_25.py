from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.5, cubic=True)
atoms.calc = EMT()

e0 = atoms.get_potential_energy()
cell0 = atoms.cell.lengths()

print(f"Before optimization: cell = {cell0}, energy = {e0:.6f} eV")

filt = FrechetCellFilter(atoms)
opt = BFGS(filt, logfile='-')
opt.run(fmax=0.01)

e1 = atoms.get_potential_energy()
cell1 = atoms.cell.lengths()

print(f"After optimization:  cell = {cell1}, energy = {e1:.6f} eV")
