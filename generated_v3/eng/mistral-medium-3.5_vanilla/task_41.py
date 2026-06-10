from ase import Atoms
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.io.trajectory import Trajectory

cu = Atoms('Cu', positions=[(0, 0, 0)], cell=[3.6, 3.6, 3.6], pbc=True)
cu.calc = EMT()
dyn = VelocityVerlet(cu, timestep=1, trajectory='md.traj')
dyn.run(10)

traj = Trajectory('md.traj')
print(len(traj), traj[-1].get_potential_energy())
