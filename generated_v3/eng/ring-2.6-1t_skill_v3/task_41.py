from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
from ase.io.trajectory import Trajectory

# create Cu FCC bulk and set EMT calculator
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# trajectory file
traj = Trajectory('cu.traj', 'w', atoms)

# MD integrator
dyn = VelocityVerlet(atoms, timestep=5 * units.fs)
dyn.attach(traj.write, interval=1)

# run 10 steps
dyn.run(10)

# read back the trajectory
traj_read = Trajectory('cu.traj')
nframes = len(traj_read)
last_frame = traj_read[-1]
print('Number of frames:', nframes)
print('Energy of last frame:', last_frame.get_potential_energy())
