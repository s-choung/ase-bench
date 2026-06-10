import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.calculators.emt import EMT

# Setup system
atoms = bulk('Cu', 'fcc', a=3.61)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

# MD Parameters
timestep = 5.0 * 1e-15  # 5 fs
n_steps = 200
t_start = 300
t_end = 600
friction = 0.01

# Initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=t_start)

# Dynamics
dyn = Langevin(atoms, timestep, temperature_K=t_start, friction=friction)

def ramp_temp():
    # Calculate temp increment per step
    delta_t = (t_end - t_start) / n_steps
    
    for i in range(n_steps):
        current_t = t_start + i * delta_t
        dyn.set_temperature(temperature_K=current_t)
        dyn.run(1)
        
        if i % 50 == 0:
            print(f"Step {i}: Temp = {atoms.get_temperature():.2f} K")

if __name__ == "__main__":
    ramp_temp()
