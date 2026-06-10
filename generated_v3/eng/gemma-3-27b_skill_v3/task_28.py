from ase import Atoms
from ase.build import bulk
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, size=(2, 2, 2))
atoms.calc = EMT()

temperature_start = 300
temperature_end = 600
num_steps = 200
timestep = 5  # fs

# Initial temperature
MaxwellBoltzmannDistribution(atoms, temperature_K=temperature_start)
Stationary(atoms)

# Temperature ramp and MD
md = Langevin(atoms, timestep=timestep * units.fs, temperature_K=temperature_start, friction=0.01 / units.fs)
for step in range(num_steps):
    md.run(1)
    current_temp = atoms.get_temperature()
    if (step + 1) % 50 == 0:
        print(f"Step {step + 1}: Temperature = {current_temp:.2f} K")

    # Temperature ramp
    temperature = temperature_start + (temperature_end - temperature_start) * (step + 1) / num_steps
    md.temperature_K = temperature
