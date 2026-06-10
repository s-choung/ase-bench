from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

cell0 = atoms.get_cell_lengths_and_angles()
e0 = atoms.get_potential_energy()
print('Before optimization:')
print('Cell (a, b, c, alpha, beta, gamma) =', cell0)
print('Energy (eV) =', e0)

opt = BFGS(FrechetCellFilter(atoms), logfile='opt.log')
opt.run(fmax=0.01)

cell1 = atoms.get_cell_lengths_and_angles()
e1 = atoms.get_potential_energy()
print('After optimization:')
print('Cell (a, b, c, alpha, beta, gamma) =', cell1)
print('Energy (eV) =', e1)
