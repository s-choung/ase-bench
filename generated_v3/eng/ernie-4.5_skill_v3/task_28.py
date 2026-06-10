from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
import numpy as np

# Create Cu FCC supercell
atoms = bulk('Cu', 'fcc', cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Set up Langevin MD with temperature ramp
timestep = 5 * units.fs
total_steps = 200
temp_start = 300
temp_end = 600

# Initialize velocities for starting temperature
atoms.set_temperature(temp_start)  # Alternatively: MaxwellBoltzmannDistribution

# Create MD object with initial temperature
md = Langevin(atoms, 
              timestep=timestep,
              temperature_K=lambda t: np.linspace(temp_start, temp_end, total_steps)[min(t, total_steps-1)],  # Temp ramp
              friction=0.01 / units.fs)

# Run MD and print temperature every 50 steps
for step in range(total_steps):
    md.run(1)  # Run 1 step at a time
    if step % 50 == 0:
        temp = atoms.get_temperature()
        print(f"Step {step}: Temperature = {temp:.2f} K")
