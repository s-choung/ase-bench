from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md import MaxwellBoltzmannDistribution
from ase.io import Trajectory, read

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.615)
atoms.calc = EMT()

# Initialize velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Set up MD
dt = 5.0  # fs
dyn = VelocityVerlet(atoms, dt * 1e-3)  # convert to ASE time units (ps)
traj = Trajectory('cu.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)

# Run 10 MD steps
dyn.run(10)
traj.close()

# Read trajectory back
frames = read('cu.traj', index=':')
print('Number of frames:', len(frames))
print('Energy of last frame (eV):', frames[-1].get_potential_energy())
