from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import Trajectory, read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

traj = Trajectory('md.traj', 'w', atoms)
md = VelocityVerlet(atoms, timestep=1 * units.fs)
md.attach(traj, interval=1)
md.run(10)

frames = read('md.traj', index=':')
print(f"Number of frames: {len(frames)}")
print(f"Energy of last frame: {frames[-1].get_potential_energy():.6f} eV")
