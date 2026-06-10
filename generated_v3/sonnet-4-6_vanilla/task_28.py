from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat(2)
atoms.calc = EMT()

T_start = 300
T_end = 600
total_steps = 200
timestep = 5 * units.fs
friction = 0.02

MaxwellBoltzmannDistribution(atoms, temperature_K=T_start)

dyn = Langevin(atoms, timestep, temperature_K=T_start, friction=friction)

step_interval = 50

for i in range(0, total_steps, step_interval):
    current_T = T_start + (T_end - T_start) * i / total_steps
    dyn.set_temperature(temperature_K=current_T)
    dyn.run(step_interval)
    actual_T = atoms.get_temperature()
    print(f"Step {i + step_interval:4d} | Target T: {current_T + (T_end - T_start) * step_interval / total_steps:.1f} K | Actual T: {actual_T:.1f} K")
