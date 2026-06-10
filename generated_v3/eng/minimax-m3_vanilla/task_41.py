from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.io import Trajectory
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

traj = Trajectory('cu_md.traj', 'w')
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs, trajectory=traj)
dyn.run(10)
traj.close()

traj = Trajectory('cu_md.traj', 'r')
print(f"Total frames: {len(traj)}")
print(f"Energy of last frame: {traj[-1].get_potential_energy():.4f} eV")
traj.close()
