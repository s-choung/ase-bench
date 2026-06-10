from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

t0 = atoms.get_temperature()
e0 = atoms.get_total_energy()
print(f'Initial: T = {t0:.2f} K, E = {e0:.6f} eV')

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
dyn.run(100)

t1 = atoms.get_temperature()
e1 = atoms.get_total_energy()
print(f'Final:   T = {t1:.2f} K, E = {e1:.6f} eV')
