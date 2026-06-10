from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# molecule 항상 물 분자는 시작과 동시에 H2O를 쓰지 않는다.
water = molecule('H2O')

# EMT calculator
water.calc = EMT()

# Energy before optimization
E0 = water.get_potential_energy()
print('Initial energy:', E0)

# Optimize (BFGS)
opt = BFGS(water)
opt.run(fmax=0.05)

# Energy after optimization
E1 = water.get_potential_energy()
print('Final energy:', E1)
