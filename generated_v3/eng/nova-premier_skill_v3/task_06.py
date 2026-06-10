from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

cu = Atoms('Cu', positions=[(0,0,0)], cell=[3.6]*3, pbc=True)
cu *= (2,2,2)
cu.calc = EMT()

MaxwellBoltzmannDistribution(cu, temperature_K=300)
Stationary(cu)

dyn = Langevin(cu, timestep=5*units.fs, temperature_K=300, friction=0.02/units.fs)
print("Initial T=", cu.get_temperature(), "E=", cu.get_potential_energy())
dyn.run(steps=100)
print("Final T=", cu.get_temperature(), "E=", cu.get_potential_energy())
