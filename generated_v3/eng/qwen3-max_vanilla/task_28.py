from ase import Atoms
from ase.build import bulk
from ase.md.langevin import Langevin
from ase.units import fs
import numpy as np

# Create Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))

# Set EMT calculator
from ase.calculators.emt import EMT
atoms.calc = EMT()

# Initialize Langevin dynamics
dyn = Langevin(atoms, 5 * fs, temperature_K=300, friction=0.002)

# Temperature ramp parameters
n_steps = 200
temp_start = 300.0
temp_end = 600.0

for step in range(n_steps):
    # Update temperature linearly
    current_temp = temp_start + (temp_end - temp_start) * step / (n_steps - 1)
    dyn.set_temperature(temperature_K=current_temp)
    
    # Run one MD step
    dyn.run(1)
    
    # Print temperature every 50 steps
    if step % 50 == 0:
        temp = atoms.get_temperature()
        print(f"Step {step}: {temp:.2f} K")
