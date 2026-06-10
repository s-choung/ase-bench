from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import Trajectory
import ase.units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = VelocityVerlet(atoms, timestep=5 * ase.units.fs)
traj = Trajectory('cu_md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)

frames = list(Trajectory('cu_md.traj', 'r'))
print(f"Total frames: {len(frames)}")
print(f"Energy of last frame: {frames[-1].get_potential_energy():.4f} eV")
