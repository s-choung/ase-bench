from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io.trajectory import Trajectory
from ase.io import read

# Create and prepare Cu FCC bulk system
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2,2,2))
atoms.calc = EMT()

# Initialize velocities for MD
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Set up MD and trajectory writer
md = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
traj = Trajectory('cu_md.traj', 'w', atoms)
md.attach(traj.write, interval=1)

# Run 10 MD steps
md.run(10)

# Read trajectory and output required values
traj_frames = read('cu_md.traj', index=':')
print(f"Total number of frames: {len(traj_frames)}")
print(f"Last frame potential energy: {traj_frames[-1].get_potential_energy():.4f} eV")
