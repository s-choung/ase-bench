from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory
from ase.io import read

# Create FCC Cu bulk
atoms = bulk('Cu', 'fcc')
atoms.set_calculator(EMT())

# Set up MD simulation
dyn = VelocityVerlet(atoms, timestep=1.0)  # 1 fs timestep
traj = Trajectory('cu_md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)

# Run 10 MD steps
dyn.run(10)

# Read trajectory and output results
traj_frames = read('cu_md.traj', index=':')
print(f"Total number of frames: {len(traj_frames)}")
print(f"Last frame potential energy: {traj_frames[-1].get_potential_energy():.3f} eV")
