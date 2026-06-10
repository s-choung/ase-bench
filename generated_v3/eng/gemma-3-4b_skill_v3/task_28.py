import numpy as np
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase.build import bulk, make_supercell
from ase.units import kB, fs, ps
from ase.positions import atoms_to_positions

# Create a Cu FCC 2x2x2 supercell
a = 3.615
atoms = bulk('Cu', 'fcc', a=a, cubic=True, orthorhombic=True)
atoms = make_supercell(atoms, (2, 2, 2), shift=(0, 0, 0))
atoms.calc = EMT()

# Set up Langevin MD
temperature = 300.0
timestep = 5 * fs
friction = 0.01 / fs  # Friction coefficient
dt = timestep
trajectory = "langevin_ramp.traj"
thermo_trajectory = "langevin_ramp_temp.traj"

# Create Langevin MD object
langevin = Langevin(atoms, timestep=dt, temperature_K=temperature, friction=friction)

# Run MD for 200 steps
for i in range(200):
    langevin.run(1)
    if (i + 1) % 50 == 0:
        temp = atoms.get_temperature()
        print(f"Step: {i+1}, Temperature: {temp:.2f} K")

# Save the trajectory
trajectory = "langevin_ramp.traj"
with open(trajectory, "w") as traj_file:
    traj = Trajectory(trajectory, "w", atoms)
    traj.write()

# Save Thermochemistry
thermo_trajectory = "langevin_ramp_temp.traj"
thermo = []
thermo.append(atoms.get_temperature())
with open(thermo_trajectory, "w") as thermo_file:
    thermo_file.write(f"{thermo[0]:.2f}\n")
