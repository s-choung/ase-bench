from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.io import Trajectory

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.set_calculator(EMT())

traj = Trajectory('md.traj', 'w')
dyn = Langevin(atoms, 1.0, temperature_K=300, friction=0.02, trajectory=traj)
dyn.run(10)
traj.close()

traj = Trajectory('md.traj')
print(len(traj), traj[-1].get_potential_energy())
