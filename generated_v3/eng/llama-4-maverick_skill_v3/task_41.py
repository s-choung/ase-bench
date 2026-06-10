from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

dyn = VelocityVerlet(atoms, timestep=5*units.fs)
traj = Trajectory('md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)

dyn.run(10)

traj_read = Trajectory('md.traj', 'r')
print(len(traj_read))
last_frame = traj_read[-1]
print(last_frame.get_potential_energy())
