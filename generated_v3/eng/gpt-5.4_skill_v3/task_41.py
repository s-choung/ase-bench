from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io import read
from ase.io.trajectory import Trajectory
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

trajfile = 'cu_md.traj'
traj = Trajectory(trajfile, 'w', atoms)

dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.attach(traj.write, interval=1)
traj.write()
dyn.run(10)
traj.close()

frames = read(trajfile, index=':')
print(len(frames))
print(frames[-1].get_potential_energy())
