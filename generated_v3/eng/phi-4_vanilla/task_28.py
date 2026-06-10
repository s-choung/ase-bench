from ase import Atoms
from ase.build import bulk
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import fs, kB
from ase.io import Trajectory

# Create a Cu FCC 2x2x2 supercell
cu = bulk('Cu', 'fcc', a=3.6)
supercell = cu.repeat((2, 2, 2))

# Set up the simulation
system = Atoms(supercell)
MaxwellBoltzmannDistribution(system, 300 * kB)  # Initialize velocities at 300K
dyn = Langevin(system, 5 * fs, temperature=300 * kB, friction=0.02)

# Set initial and final temperatures
T0 = 300 * kB
T1 = 600 * kB

# Run the simulation with a temperature ramp
n_steps = 200
print_interval = 50

traj = Trajectory('md.traj', 'w', system)
for step in range(n_steps):
    if step % print_interval == 0:
        dyn.set_temperature(T0 + step * (T1 - T0) / n_steps)
        print(f"Step {step}, Temperature: {dyn.temperature/kB:.2f} K")
    dyn.run(1)
    traj.write(system)

traj.close()
