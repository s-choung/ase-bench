from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print('Initial T:', atoms.get_temperature())
print('Initial E:', atoms.get_potential_energy())

md = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.002 / units.fs)
md.run(100)

print('Final T:', atoms.get_temperature())
print('Final E:', atoms.get_potential_energy())
