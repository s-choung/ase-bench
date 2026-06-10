from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()
print(atoms.cell.lengths(), atoms.get_potential_energy())
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)
print(atoms.cell.lengths(), atoms.get_potential_energy())
