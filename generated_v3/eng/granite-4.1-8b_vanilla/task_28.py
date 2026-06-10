from ase import Atoms
from ase.build import fcc111
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
import numpy as np

# Create Cu FCC 2x2x2 supercell
size = 2
cells = fcc111('Cu', size=(size, size, size), vacuum=10)
atoms = cells

# Set calculator
atoms.set_calculator(EMT())

# Define temperature ramp
initial_temp = 300.0  # K
final_temp = 600.0    # K
num_steps = 200
dt = 5e-3             # 5 fs in seconds

# Langevin dynamics with temperature ramp
md = Langevin(atoms, 5 * 2 * np.pi / (3.15576e13 * size**2), initial_temp, 1.0,
             _tslice=dt)

def temperature_ramp(t):
    return initial_temp + (final_temp - initial_temp) * (t / md.timestep)

def set_ramp_temperature(atoms, t):
    T = temperature_ramp(t)
    md.set_temperature(T)

md.attach(set_ramp_temperature, 0)

# Print temperature every 50 steps
@md.event_wrapped(atoms=numpy.array(range(0, num_steps, 50)))
def print_temperature(atoms, md):
    print(f'Step {md.step}: Temperature = {md.temperature:.2f} K')

# Run the MD simulation
md.run(num_steps)
