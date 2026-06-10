from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

T0, T1 = 300.0, 600.0
steps = 200
dt = 5 * units.fs

MaxwellBoltzmannDistribution(atoms, temperature_K=T0)
Stationary(atoms)

dyn = Langevin(
    atoms,
    timestep=dt,
    temperature_K=T0,
    friction=0.01 / units.fs,
)

for step in range(1, steps + 1):
    target_T = T0 + (T1 - T0) * (step - 1) / (steps - 1)
    dyn.set_temperature(temperature_K=target_T)
    dyn.run(1)

    if step % 50 == 0:
        print(f"Step {step}: T = {atoms.get_temperature():.2f} K")
