import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Setup system
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# MD parameters
timestep = 5 * units.fs
n_steps = 200
t_start, t_end = 300, 600

# Setup Langevin dynamics
dyn = Langevin(atoms, timestep=timestep, temperature_K=t_start, friction=0.01/units.fs)

for step in range(n_steps):
    # Linear temperature ramp
    current_t = t_start + (t_end - t_start) * (step / n_steps)
    dyn.set_temperature(temperature_K=current_t)
    
    dyn.run(1)
    
    if step % 50 == 0:
        print(f"Step {step}: Temp = {atoms.get_temperature():.2f} K")
