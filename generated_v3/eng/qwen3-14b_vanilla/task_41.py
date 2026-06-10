from ase import Atoms, bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.io.trajectory import Trajectory

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()
traj = Trajectory('cu_md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, dt=1.0, trajectory=traj)
dyn.run(10)
traj = Trajectory('cu_md.traj', 'r')
print(len(traj))
print(traj[-1].get_potential_energy())
