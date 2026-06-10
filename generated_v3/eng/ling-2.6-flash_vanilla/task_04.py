from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

water = Atoms('H2O', positions=[[0, 0, 0], [0.757, 0.586, 0.0], [-0.757, 0.586, 0.0]])
water.set_calculator(EMT())

print('Energy before optimization:', water.get_potential_energy())

optimizer = BFGS(water)
optimizer.run(fmax=0.05)

print('Energy after optimization:', water.get_potential_energy())
