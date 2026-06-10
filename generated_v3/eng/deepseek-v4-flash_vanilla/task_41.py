from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.io import read, write

# Build Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.61)

# Attach EMT calculator
atoms.calc = EMT()

# Set initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Set up MD (Velocity Verlet, 1 fs time step, 10 steps)
dyn = VelocityVerlet(atoms, dt=1.0 * units.fs)

# Attach trajectory writer
traj_file = 'md.traj'
dyn.attach(write, interval=1, filename=traj_file, images=atoms)

# Run 10 steps
dyn.run(steps=10)

# Read trajectory back
frames = read(traj_file, index=':')
print(f'Total frames: {len(frames)}')
print(f'Energy of last frame: {frames[-1].get_potential_energy():.4f} eV')
