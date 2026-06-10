from ase.calculators.emt import EMT
from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory
from ase.io import read
from ase import units

# Create Cu FCC bulk and attach EMT calculator
atoms = bulk('Cu', 'fcc', cubic=True)
atoms.calc = EMT()

# Run short MD (10 steps) and save to trajectory
traj = Trajectory('md.traj', 'w', atoms)
md = VelocityVerlet(atoms, timestep=5 * units.fs)
md.attach(traj.write, interval=1)
md.run(10)

# Read trajectory back and print information
trajectory = read('md.traj', '@:')
print(f'Total frames: {len(trajectory)}')
print(f'Last frame energy: {trajectory[-1].get_potential_energy():.3f} eV')
