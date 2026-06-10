from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory
from ase.io import read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

md = VelocityVerlet(atoms, timestep=5*units.fs, trajectory='md.traj')
md.run(10)

traj = read('md.traj', index=':')
print(f"Total frames: {len(traj)}")
print(f"Last frame energy: {traj[-1].get_potential_energy():.6f} eV")
