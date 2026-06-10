from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import read
from ase.io.trajectory import Trajectory

# Build Cu FCC bulk and attach EMT
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initialise velocities (300 K) and remove COM motion
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# MD (NVE) for 10 steps, saving each frame
dyn = VelocityVerlet(atoms, timestep=1 * units.fs)
traj = Trajectory('md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)
traj.close()

# Read trajectory and report frames & last energy
frames = read('md.traj', index=':')
print(len(frames), frames[-1].get_potential_energy())
