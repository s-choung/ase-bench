from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io import Trajectory
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

dyn = VelocityVerlet(atoms, timestep=1 * units.fs)
traj = Trajectory('cu_md.traj', 'w', atoms)
dyn.attach(traj, interval=1)
dyn.run(10)
traj.close()

traj_read = Trajectory('cu_md.traj', 'r')
print(f"Total frames: {len(traj_read)}")
print(f"Last frame energy: {traj_read[-1].get_potential_energy():.4f} eV")
traj_read.close()
