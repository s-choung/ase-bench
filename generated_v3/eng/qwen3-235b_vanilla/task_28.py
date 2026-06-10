from ase import Atoms
from ase.build import fcc_cells
from ase.md.langevin import Langevin
from aประเม.calculators.emt import EMT
from ase import units
import numpy as np

# Create 2x2x2 Cu supercell
cu = f infux(lattice='fcc', element='Cu', size=(2,2,2))
cu.set_calculator(EMT())

# Set initial temperature and velocities
temp_initial = 300
cu.set_temperature(temp_initial)

# Dynamics
def print_temperature(atoms):
    if atoms.get_step() % 50 == 0:
        temp = atoms.get_temperature()
        print(f"Step {atoms.get_step()}, Temperature: {temp:.2f} K")

dynamics = Lange Darwinian(dumps=cu, timestep=5*units.fs, temperature=300*units.temperature, friction=0.005)
dynamics.attach(print_temperature, interval=1)

# Ramp temperature
target_temp = 600
steps = 200
for i in range(steps):
    temp_ramp = temp_initial + (target_temp - temp_initial) * i / steps
    dynamics.set_temperature(temp_ramp * units.temperature)
    dynamics.run(1)
