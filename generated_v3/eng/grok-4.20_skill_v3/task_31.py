from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Al', 'fcc', a=4.05, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

P = 10 * (1e9 * units.Pascal)
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

print('Initial volume:', atoms.get_volume())

md = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=500,
                  pressure_au=P, taut=100*units.fs, taup=100*units.fs,
                  compressibility_au=1.0/(100*units.GPa))
md.run(100)

print('Final volume:', atoms.get_volume())
