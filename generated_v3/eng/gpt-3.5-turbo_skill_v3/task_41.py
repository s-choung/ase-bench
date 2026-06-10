from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.io import write, read, Trajectory

# Create a Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.5)

# Attach EMT calculator
atoms.calc = EMT()

# Set initial velocities based on Maxwell-Boltzmann distribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Run MD for 10 steps
dyn = VelocityVerlet(atoms, timestep=1 * atoms.get_calculator().calc.get_time_step())
traj = Trajectory('md.traj', 'w', atoms)
for i in range(10):
    dyn.run(10)
    traj.write(atoms)

# Read the trajectory back
traj = read('md.traj', 'index:')
total_frames = len(traj)
energy_last_frame = traj[-1].get_potential_energy()

print(f"Total number of frames: {total_frames}")
print(f"Energy of the last frame: {energy_last_frame} eV")
