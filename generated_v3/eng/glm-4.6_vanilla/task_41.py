from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.io import Trajectory

atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

dyn = Langevin(atoms, timestep=1.0e-15, temperature=300, friction=0.002)
traj = Trajectory('cu_md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)

traj_read = Trajectory('cu_md.traj', 'r')
print(f"Total frames: {len(traj_read)}")
print(f"Last frame energy: {traj_read[-1].get_potential_energy()}")
