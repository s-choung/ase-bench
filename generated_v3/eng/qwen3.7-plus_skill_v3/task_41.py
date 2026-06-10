from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io.trajectory import Trajectory
from ase.io import read
import ase.units as units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

traj = Trajectory('md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, timestep=1 * units.fs, trajectory=traj)
dyn.run(steps=10)
traj.close()

frames = read('md.traj', index=':')
print(f"Total frames: {len(frames)}")
print(f"Energy of last frame: {frames[-1].get_potential_energy():.6f} eV")
