from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

print("Initial Cell:\n", atoms.get_cell())
print("Initial Energy:", atoms.get_potential_energy())

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print("Final Cell:\n", atoms.get_cell())
print("Final Energy:", atoms.get_potential_energy())
