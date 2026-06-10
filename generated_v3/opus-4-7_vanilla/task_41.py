from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory
from ase.io import read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
traj = Trajectory('cu_md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
traj.write(atoms)
dyn.run(10)
traj.close()

frames = read('cu_md.traj', index=':')
print("Total frames:", len(frames))
print("Last frame energy:", frames[-1].get_potential_energy())
