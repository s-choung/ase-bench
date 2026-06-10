from ase.build import bulk
from ase.calculators.emt import EMT
from ase import Atoms
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io.trajectory import Trajectory
from ase.md.verlet import VelocityVerlet

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)

# Attach EMT calculator
atoms.calc = EMT()

# Set initial velocities
MaxwellBoltzmannDistribution(atoms, temperature=300)

# Run MD and save trajectory
dyn = VelocityVerlet(atoms, 1 * 1e-15)
traj = Trajectory('cu_md.traj', 'w', atoms)

for step in range(10):
    dyn.run(1)
    traj.write()

# Read trajectory and analyze
traj = Trajectory('cu_md.traj', 'r')
print("Total frames:", len(traj))
print("Energy of last frame:", traj[-1].get_potential_energy())
