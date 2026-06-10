from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.io.trajectory import Trajectory
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
dyn = VelocityVerlet(atoms, timestep=5*units.fs)
traj = Trajectory('cu_traj.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)

read_traj = Trajectory('cu_traj.traj')
print(f'Frames: {len(read_traj)}')
last_atoms = read_traj[-1]
print(f'Energy: {last_atoms.get_potential_energy():.3f} eV')
