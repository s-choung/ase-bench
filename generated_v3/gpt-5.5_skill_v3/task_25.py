from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk("Cu", "fcc", a=3.6, cubic=True)
atoms.calc = EMT()

print("Initial cell lengths/angles:", atoms.cell.cellpar())
print("Initial energy (eV):", atoms.get_potential_energy())

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print("Final cell lengths/angles:", atoms.cell.cellpar())
print("Final energy (eV):", atoms.get_potential_energy())
print("Final positions (Ang):")
print(atoms.positions)
