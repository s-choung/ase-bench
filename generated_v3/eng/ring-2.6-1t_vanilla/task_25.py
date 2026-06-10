from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import FrechetCellFilter
from ase.optimize import BFGS

# Create Cu FCC with an initial guess for the lattice constant
cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()

# before optimisation
print('Before optimisation')
print('Cell:', cu.get_cell())
print('Energy:', cu.get_potential_energy())

# combine cell and atomic relaxation
filtered = FrechetCellFilter(cu)

# optimise with BFGS until forces < 0.01 eV/Å
opt = BFGS(filtered)
opt.run(fmax=0.01)

# after optimisation
print('\nAfter optimisation')
print('Cell:', cu.get_cell())
print('Energy:', cu.get_potential_energy())
