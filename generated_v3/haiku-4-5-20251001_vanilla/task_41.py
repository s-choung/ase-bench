from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannVelocityDistribution
from ase.md.verlet import VelocityVerlet
from ase.io import read, Trajectory
from ase.units import fs

# Create Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.61)

# Attach EMT calculator
atoms.calc = EMT()

# Set initial velocities
MaxwellBoltzmannVelocityDistribution(atoms, temperature_K=300)

# Create trajectory file
traj = Trajectory('cu_md.traj', 'w', atoms)

# Run MD for 10 steps
md = VelocityVerlet(atoms, dt=5*fs)
for i in range(10):
    md.run(1)
    traj.write(atoms)

traj.close()

# Read trajectory and get information
traj_read = read('cu_md.traj', index=':')
if isinstance(traj_read, list):
    frames = traj_read
else:
    frames = [traj_read]

print(f"Total frames: {len(frames)}")
print(f"Energy of last frame: {frames[-1].get_potential_energy():.6f} eV")
