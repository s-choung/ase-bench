from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

T_start, T_end = 300.0, 600.0
total_steps = 200
timestep = 5 * units.fs

MaxwellBoltzmannDistribution(atoms, temperature_K=T_start)
Stationary(atoms)

dyn = Langevin(atoms, timestep=timestep, temperature_K=T_start, friction=0.01 / units.fs)

for step in range(total_steps):
    T_target = T_start + (T_end - T_start) * step / (total_steps - 1)
    dyn.target = T_target * units.kB
    dyn.run(1)
    if step % 50 == 0:
        print(f"Step {step:4d} | Target: {T_target:7.1f} K | Actual: {atoms.get_temperature():7.1f} K")

print(f"Step {total_steps-1:4d} | Target: {T_end:7.1f} K | Actual: {atoms.get_temperature():7.1f} K")
