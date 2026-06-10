from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

e0 = atoms.get_potential_energy()
c0 = atoms.cell.lengths()
print('Before optimization:')
print('Cell lengths (A):', c0)
print('Energy (eV):', e0)

ecf = FrechetCellFilter(atoms)
opt = BFGS(ecf, logfile=None)
opt.run(fmax=0.01)

e1 = atoms.get_potential_energy()
c1 = atoms.cell.lengths()
print('After optimization:')
print('Cell lengths (A):', c1)
print('Energy (eV):', e1)
