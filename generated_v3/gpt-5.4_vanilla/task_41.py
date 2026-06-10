from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

traj = Trajectory('cu_md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.attach(traj.write, interval=1)
dyn.run(10)
traj.close()

frames = Trajectory('cu_md.traj', 'r')
nframes = len(frames)
last = frames[-1]
last.calc = EMT()

print(nframes)
print(last.get_potential_energy())
