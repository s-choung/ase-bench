from ase import units
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory
from ase.calculators.emt import EMT
from ase.build import bulk

# Create Cu FCC bulk and attach EMT calculator
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initialize MD and trajectory
dyn = VelocityVerlet(atoms, 5 * units.fs)
traj = Trajectory('cu_md.traj', 'w', atoms)

# Run MD for 10 steps
for step in range(10):
    dyn.run(1)
    traj.write()

# Read trajectory and analyze
traj = Trajectory('cu_md.traj')
print(f"Number of frames: {len(traj)}")
last_frame = traj[-1]
print(f"Energy of last frame: {last_frame.get_potential_energy():.4f} eV")
