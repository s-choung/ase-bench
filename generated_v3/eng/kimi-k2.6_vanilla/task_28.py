from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', cubic=True) * [2, 2, 2]
atoms.calc = EMT()

dt = 5.0 * units.fs
T1, T2 = 300.0, 600.0
n_steps = 200
friction = 0.01

MaxwellBoltzmannDistribution(atoms, temperature_K=T1)
dyn = Langevin(atoms, dt, T1 * units.kB, friction)

for i in range(n_steps):
    dyn.temp = (T1 + (T2 - T1) * i / (n_steps - 1)) * units.kB
    dyn.run(1)
    if i % 50 == 0:
        print(f"Step {i}: T = {atoms.get_temperature():.1f} K")
