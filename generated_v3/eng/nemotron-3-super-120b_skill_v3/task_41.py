from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet
from ase.io import Trajectory, read

# Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# MD with trajectory output
traj = Trajectory('cu_md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, timestep=5*units.fs, trajectory=traj)
dyn.run(10)
traj.close()

# Read trajectory and report
frames = read('cu_md.traj', index=':')
print('Number of frames:', len(frames))
print('Energy of last frame (eV):', frames[-1].get_potential_energy())
