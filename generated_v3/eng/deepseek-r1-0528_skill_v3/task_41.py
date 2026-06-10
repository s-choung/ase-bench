from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory

# Create FCC Cu structure
atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

# Set up MD parameters
timestep = 5.0 * units.fs
temperature = 300  # Kelvin
duration = 10 * timestep

# Initialize velocity distribution
MaxwellBoltzmannDistribution(atoms, temperature_K=temperature)
Stationary(atoms)  # Remove COM motion

# Run MD with trajectory recording
traj_file = 'cu_md.traj'
traj = Trajectory(traj_file, 'w', atoms)
dyn = VelocityVerlet(atoms, timestep)
dyn.attach(traj.write, interval=1)
dyn.run(steps=10)
traj.close()

# Read trajectory and analyze
traj = Trajectory(traj_file, 'r')
print("Total frames:", len(traj))
last_atoms = traj[-1]
print("Last frame energy:", last_atoms.get_potential_energy(), "eV")
