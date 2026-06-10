from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Initial structure
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Cell and energy before optimization
cell0 = atoms.get_cell_lengths_and_angles()
energy0 = atoms.get_potential_energy()
print('Before optimization:')
print('Cell:', cell0)
print('Energy:', energy0)

# Simultaneous cell+position optimization
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Cell and energy after optimization
cell1 = atoms.get_cell_lengths_and_angles()
energy1 = atoms.get_potential_energy()
print('\nAfter optimization:')
print('Cell:', cell1)
print('Energy:', energy1)
