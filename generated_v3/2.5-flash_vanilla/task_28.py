from ase import build
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
import numpy as np

# 1. System setup
atoms = build.bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

# 2. MD parameters
timestep = 5 * units.fs
total_steps = 200
initial_temp = 300  # K
final_temp = 600    # K
damping = 0.1 * units.ps # Damping parameter for Langevin

# Initialize velocities at initial temperature
atoms.set_velocities(np.random.normal(0, np.sqrt(initial_temp * units.kB / atoms.get_masses()[0]), (len(atoms), 3)))

# 3. Langevin dynamics setup
dyn = Langevin(atoms, timestep, initial_temp * units.kB, damping)

# 4. Temperature ramp
temp_increment_per_step = (final_temp - initial_temp) / total_steps

print(f"Starting MD simulation with temperature ramp from {initial_temp}K to {final_temp}K over {total_steps} steps.")
print(f"Timestep: {timestep/units.fs:.0f} fs, Damping: {damping/units.ps:.1f} ps")

for step in range(1, total_steps + 1):
    current_target_temp = initial_temp + temp_increment_per_step * step
    dyn.temperature_K = current_target_temp # Update target temperature for Langevin

    dyn.run(1) # Run one step

    if step % 50 == 0:
        print(f"Step: {step}/{total_steps}, Current target temperature: {current_target_temp:.2f} K")

print("MD simulation finished.")
