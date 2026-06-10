from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.io import Trajectory, read

# Create Cu FCC bulk
cu = Atoms('Cu4', positions=[(0, 0, 0), (0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0)],
           cell=[1, 1, 1], pbc=True)
cu.set_calculator(EMT())

# Initialize velocities and dynamics
MaxwellBoltzmannDistribution(cu, temperature_K=300)
dyn = VelocityVerlet(cu, dt=1)

# Run MD and save to trajectory
traj = Trajectory('cu_md.traj', 'w')
dyn.attach(traj.write, interval=1)
dyn.run(10)

# Read trajectory and print info
traj = read('cu_md.traj', index=':')
print(f'Number of frames: {len(traj)}')
print(f'Energy of last frame: {traj[-1].get_potential_energy()}')
