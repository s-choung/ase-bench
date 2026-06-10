from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk("Cu", "fcc", a=3.6, cubic=True)
atoms.calc = EMT()

print("Before optimization:")
print("Cell lengths/angles:", atoms.cell.cellpar())
print("Energy (eV):", atoms.get_potential_energy())

opt = BFGS(FrechetCellFilter(atoms), logfile=None)
opt.run(fmax=0.01)

print("\nAfter optimization:")
print("Cell lengths/angles:", atoms.cell.cellpar())
print("Energy (eV):", atoms.get_potential_energy())
