from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

nsteps = 200
dyn = Langevin(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    friction=0.01 / units.fs,
)

for step in range(1, nsteps + 1):
    target_T = 300 + (600 - 300) * step / nsteps
    dyn.set_temperature(temperature_K=target_T)
    dyn.run(1)

    if step % 50 == 0:
        print(f"Step {step}: T = {atoms.get_temperature():.2f} K")
