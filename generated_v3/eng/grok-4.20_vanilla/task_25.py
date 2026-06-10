from ase.build import bulk
from ase.optimize import BFGS
from ase.constraints import FrechetCellFilter
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print('Before:')
print('Cell size:', atoms.cell[0,0])
print('Energy:   ', atoms.get_potential_energy())

cf = FrechetCellFilter(atoms)
opt = BFGS(cf)
opt.run(fmax=0.01)

print('After:')
print('Cell size:', atoms.cell[0,0])
print('Energy:   ', atoms.get_potential_energy())
