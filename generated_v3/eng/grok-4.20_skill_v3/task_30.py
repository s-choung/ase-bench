from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True).repeat((3, 3, 3))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print('Initial volume:', atoms.get_volume())
print('Initial pressure:', atoms.get_pressure() / units.bar)

md = NPTBerendsen(atoms, timestep=5 * units.fs, temperature_K=300, pressure_au=1 * units.bar,
                  taut=100 * units.fs, taup=1000 * units.fs)
md.run(200)

print('Final volume:', atoms.get_volume())
print('Final pressure:', atoms.get_pressure() / units.bar)
