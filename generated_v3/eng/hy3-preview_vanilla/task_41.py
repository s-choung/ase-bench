from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase import units
from ase.io import Trajectory

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initialize velocities and run MD
atoms.set_velocities(1e-1 * (2 * (0.5 - np.random.random((len(atoms), 3)))))
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
traj = Trajectory('md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)
traj.close()

# Read trajectory and print info
traj_read = Trajectory('md.traj')
print(f"Total frames: {len(traj_read)}")
print(f"Energy of last frame: {traj_read[-1].get_potential_energy():.3f} eV")
