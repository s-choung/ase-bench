from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import Trajectory
import ase.units as units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
md = VelocityVerlet(atoms, timestep=5*units.fs)
traj = Trajectory('md.traj', 'w', atoms)
md.attach(traj.write, interval=1)
md.run(10)
traj.close()
traj_read = Trajectory('md.traj', 'r')
n_frames = len(traj_read)
last_energy = traj_read[-1].get_potential_energy()
print(f'Total frames: {n_frames}')
print(f'Last frame energy: {last_energy:.4f} eV')
traj_read.close()
