from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.5, cubic=True)
atoms.calc = EMT()

print("Before optimization:")
print("cell =", atoms.get_cell())
print("energy =", atoms.get_potential_energy())

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print("After optimization:")
print("cell =", atoms.get_cell())
print("energy =", atoms.get_potential_energy())
