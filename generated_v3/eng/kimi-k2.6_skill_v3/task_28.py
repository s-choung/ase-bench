from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)

for i in range(200):
    if i % 50 == 0:
        print(f"{i} {atoms.get_temperature():.1f}")
    dyn.temp = (300 + 300 * i / 199) * units.kB
    dyn.run(1)

print(f"200 {atoms.get_temperature():.1f}")
