from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import FrechetCellFilter
from ase.optimize import BFGS

a0 = 3.60  # initial lattice constant
atoms = bulk('Cu', 'fcc', a=a0)
atoms.calc = EMT()

print('Before optimization:')
print('Cell:', atoms.cell.lengths())
print('Energy:', atoms.get_potential_energy())

fccf = FrechetCellFilter(atoms)
opt = BFGS(fccf)
opt.run(fmax=0.01)

print('\nAfter optimization:')
print('Cell:', atoms.cell.lengths())
print('Energy:', atoms.get_potential_energy())
