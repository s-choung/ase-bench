from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initialize MD with trajectory
traj = Trajectory('md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, timestep=5 * units.fs)

for _ in range(10):
    dyn.run(1)
    traj.write(atoms)

traj.close()

# Read trajectory
traj = Trajectory('md.traj')
print(len(traj))
print(traj[-1].get_potential_energy())
