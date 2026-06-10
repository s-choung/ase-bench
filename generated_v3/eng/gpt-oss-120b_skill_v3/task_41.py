from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import read
from ase.io.trajectory import Trajectory
from ase import units

# Cu FCC bulk with EMT
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# MD settings
dyn = VelocityVerlet(atoms, timestep=5 * units.fs)
traj = Trajectory('md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)

# Run 10 MD steps
dyn.run(10)

# Read trajectory and report
frames = read('md.traj', index=':')
print(len(frames), frames[-1].get_potential_energy())
