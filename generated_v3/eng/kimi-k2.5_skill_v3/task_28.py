from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dt = 5 * units.fs
dyn = Langevin(atoms, timestep=dt, temperature_K=lambda t: 300 + 0.3 * t / units.fs, friction=0.01 / units.fs)

for i in range(4):
    dyn.run(50)
    print(f"Step {(i+1)*50}, T = {atoms.get_temperature():.1f} K")
