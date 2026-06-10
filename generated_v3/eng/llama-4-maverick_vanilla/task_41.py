from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory

# Create Cu FCC bulk
cu = Atoms('Cu', positions=[[0, 0, 0]], cell=[[0, 2.7, 2.7], [2.7, 0, 2.7], [2.7, 2.7, 0]], pbc=True)
cu *= (2, 2, 2)
cu.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(cu, temperature_K=300)

# Set up MD
dyn = VelocityVerlet(cu, 1 * 0.5 * 1e-15)  # 0.5 fs time step
traj = Trajectory('cu.traj', 'w', cu)
dyn.attach(traj.write, interval=1)

# Run MD
dyn.run(10)

# Read trajectory and print info
traj = Trajectory('cu.traj', 'r')
print(len(traj))
print(traj[-1].get_potential_energy())
