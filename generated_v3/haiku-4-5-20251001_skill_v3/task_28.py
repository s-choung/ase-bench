from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

T_start = 300
T_end = 600
n_steps = 200
timestep = 5 * units.fs
friction = 0.01 / units.fs

MaxwellBoltzmannDistribution(atoms, temperature_K=T_start)
Stationary(atoms)

def temperature_ramp(step):
    return T_start + (T_end - T_start) * step / n_steps

md = Langevin(atoms, timestep=timestep, temperature_K=T_start, friction=friction)

for step in range(n_steps):
    T_current = temperature_ramp(step)
    md.set_temperature(T_current)
    md.run(1)
    
    if (step + 1) % 50 == 0:
        T_actual = atoms.get_temperature()
        print(f"Step {step + 1:3d}: Target T = {T_current:.1f} K, Actual T = {T_actual:.1f} K")
