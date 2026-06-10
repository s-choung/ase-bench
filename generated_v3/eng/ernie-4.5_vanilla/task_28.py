from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
import numpy as np

# Create FCC Cu supercell
atoms = bulk('Cu', 'fcc', cubic=True).repeat((2, 2, 2))

# Set calculator to EMT
atoms.calc = EMT()

# Define temperature ramp: from 300K to 600K over 200 steps
start_temp = 300.0
end_temp = 600.0
timestep = 5.0  # in fs

# Langevin MD
md = Langevin(atoms, 
              timestep=timestep * 1e-3,  # convert fs to ps
              temperature_K=lambda t: start_temp + (end_temp - start_temp) * t / (200 * timestep * 1e-3),  # linear ramp
              friction=0.01,
              logfile=None)

# Function to print temperature periodically
def print_temperature(step):
    if step % 50 == 0:
        temp = md.get_temperature()
        print(f"Step {step}: Temperature = {temp:.2f} K")

# Run MD and print temperature every 50 steps
for step in range(1, 201):
    md.run(1)
    print_temperature(step)
