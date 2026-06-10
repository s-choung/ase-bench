from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

dt = 5 * units.fs
nsteps = 200
T0, T1 = 300.0, 600.0
friction = 0.01 / units.fs

dyn = Langevin(atoms, timestep=dt, temperature_K=T0, friction=friction)

print(f"Step 0: target={T0:.1f} K, current={atoms.get_temperature():.1f} K")
for step in range(1, nsteps + 1):
    T = T0 + (T1 - T0) * step / nsteps
    dyn.set_temperature(temperature_K=T)
    dyn.run(1)
    if step % 50 == 0:
        print(f"Step {step}: target={T:.1f} K, current={atoms.get_temperature():.1f} K")
