from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation

atoms = bulk("Cu", "fcc", a=3.615, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

T0 = 300.0
T1 = 600.0
nsteps = 200
dt = 5.0 * units.fs

MaxwellBoltzmannDistribution(atoms, temperature_K=T0)
Stationary(atoms)
ZeroRotation(atoms)

dyn = Langevin(
    atoms,
    timestep=dt,
    temperature_K=T0,
    friction=0.01 / units.fs,
)

for step in range(1, nsteps + 1):
    target_T = T0 + (T1 - T0) * step / nsteps
    dyn.set_temperature(temperature_K=target_T)
    dyn.run(1)

    if step % 50 == 0:
        print(f"step {step}: T = {atoms.get_temperature():.2f} K, target = {target_T:.2f} K")
