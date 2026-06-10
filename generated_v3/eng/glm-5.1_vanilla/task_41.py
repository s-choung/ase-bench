from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io.trajectory import Trajectory
from ase.io import read

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

md = VelocityVerlet(atoms, 5.0)
traj = Trajectory('md.traj', 'w', atoms)
md.attach(traj.write)
md.run(steps=10)
traj.close()

frames = read('md.traj', index=':')
print(f"Total frames: {len(frames)}")
print(f"Last frame energy: {frames[-1].get_potential_energy():.4f} eV")
