from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule with approximate geometry
water = Atoms('OH2',
              positions=[(0, 0, 0), (0.96, 0, 0), (-0.24, 0.93, 0)],
              calculator=EMT())

# Print energy before optimization
print(f'Initial energy: {water.get_potential_energy():.6f} eV')

# Optimize with BFGS
opt = BFGS(water)
opt.run(fmax=0.05)

# Print energy after optimization
print(f'Final energy: {water.get_potential_energy():.6f} eV')
