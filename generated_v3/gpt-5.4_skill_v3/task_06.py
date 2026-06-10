from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

e0 = atoms.get_total_energy()
t0 = atoms.get_temperature()

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
dyn.run(100)

e1 = atoms.get_total_energy()
t1 = atoms.get_temperature()

print(f'Initial temperature: {t0:.3f} K')
print(f'Initial total energy: {e0:.6f} eV')
print(f'Final temperature: {t1:.3f} K')
print(f'Final total energy: {e1:.6f} eV')
