from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk("Cu", "fcc", a=3.6, cubic=True)
atoms.calc = EMT()

print("Before optimization")
print("Cell parameters:", atoms.cell.cellpar())
print("Energy:", atoms.get_potential_energy())

filt = FrechetCellFilter(atoms)
opt = BFGS(filt)
opt.run(fmax=0.01)

print("After optimization")
print("Cell parameters:", atoms.cell.cellpar())
print("Energy:", atoms.get_potential_energy())
