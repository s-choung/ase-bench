from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print('Initial cell size:', atoms.cell.lengths())
print('Initial energy:', atoms.get_potential_energy())

ecf = FrechetCellFilter(atoms)
opt = BFGS(ecf)
opt.run(fmax=0.01)

print('Final cell size:', atoms.cell.lengths())
print('Final energy:', atoms.get_potential_energy())
