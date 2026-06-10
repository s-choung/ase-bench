from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory
from ase.io import read

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
dyn = VelocityVerlet(atoms, timestep=5.0)

traj = Trajectory('cu_md.traj', 'w', atoms)
dyn.attach(traj.write)
dyn.run(10)
traj.close()

traj = read('cu_md.traj', index=':')
print(len(traj))
print(traj[-1].get_potential_energy())
