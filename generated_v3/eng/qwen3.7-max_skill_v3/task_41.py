from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
from ase.io.trajectory import Trajectory
from ase.io import read

atoms = bulk('Cu', 'fcc', cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

md = VelocityVerlet(atoms, timestep=5 * units.fs)
traj = Trajectory('cu_md.traj', 'w', atoms)
md.attach(traj.write, interval=1)

md.run(10)
traj.close()

frames = read('cu_md.traj', index=':')
print(f"Total frames: {len(frames)}")

last_frame = frames[-1]
last_frame.calc = EMT()
print(f"Energy of last frame: {last_frame.get_potential_energy():.4f} eV")
