from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.io import Trajectory
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Create Cu FCC bulk and attach EMT calculator
atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()

# Initialise velocities (300 K)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Set up MD and trajectory writer
dt = 1.0 * units.fs
traj = Trajectory('cu_md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, dt)
dyn.attach(traj.write, interval=1)

# Run 10 MD steps
dyn.run(10)

# Read trajectory and report
traj = Trajectory('cu_md.traj')
n_frames = len(traj)
last_energy = traj[-1].get_potential_energy()
print(f"Number of frames: {n_frames}")
print(f"Energy of last frame: {last_energy:.6f} eV")
