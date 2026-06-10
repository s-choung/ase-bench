from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
from ase.io.trajectory import Trajectory

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

trajfile = 'cu_md.traj'
traj = Trajectory(trajfile, 'w', atoms)

dyn = VelocityVerlet(atoms, timestep=1 * units.fs, trajectory=traj)
dyn.run(10)
traj.close()

traj = Trajectory(trajfile)
nframes = len(traj)
last = traj[-1]
print(nframes)
print(last.get_potential_energy())
