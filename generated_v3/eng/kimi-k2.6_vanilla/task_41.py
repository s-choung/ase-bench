from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io import Trajectory
from ase import units

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()

dyn = VelocityVerlet(atoms, 5 * units.fs)
traj = Trajectory('cu.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)
traj.close()

traj = Trajectory('cu.traj')
print(len(traj))
print(traj[-1].get_total_energy())
