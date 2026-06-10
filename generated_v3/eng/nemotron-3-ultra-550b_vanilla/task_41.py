from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md import MDLogger
from ase import units
from ase.io import Trajectory

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

trajectory = Trajectory('cu_md.traj', 'w', atoms)

dyn = VelocityVerlet(atoms, timestep=5 * units.fs)
dyn.attach(trajectory.write, interval=1)
dyn.run(10)

traj = Trajectory('cu_md.traj')
print(f"Number of frames: {len(traj)}")
print(f"Energy of last frame: {traj[-1].get_potential_energy():.4f} eV")
