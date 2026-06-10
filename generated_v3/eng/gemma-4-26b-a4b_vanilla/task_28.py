import numpy as np
from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase import units

# Setup Cu FCC 2x2x2 supercell
atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                           symbol='Cu', latticeconstant=3.6, size=(2, 2, 2))
atoms.calc = EMT()  # Using EMT as a placeholder; Cu requires EAM for accuracy

# MD Parameters
dt = 5 * units.fs
n_steps = 200
temp_start = 300
temp_end = 600

# Linear temperature ramp function
def get_temp(step):
    return temp_start + (temp_end - temp_start) * (step / n_steps)

# Langevin Dynamics setup
# friction coefficient (gamma) is arbitrary for demonstration
dyn = Langevin(atoms, timestep=dt, temperature=temp_start, friction=0.01)

def print_temp():
    current_step = dyn.get_number_of_steps()
    # Calculate target temperature for this step to ramp
    current_t = get_temp(current_step)
    dyn.set_temperature(current_t)
    print(f"Step: {current_step:3d} | Target Temp: {current_t:6.2f} K")

# Run MD
print(f"Starting ramp from {temp_start}K to {temp_end}K")
for step in range(n_steps + 1):
    if step % 50 == 0:
        print_temp()
    if step < n_steps:
        dyn.run(1)
