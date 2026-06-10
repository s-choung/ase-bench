from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase import units
from ase.io import read, Trajectory
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

traj = Trajectory('md.traj', 'w', atoms)
md = VelocityVerlet(atoms, timestep=5*units.fs, trajectory=traj)
md.run(10)
traj.close()

traj_read = read('md.traj', index=':')
print(len(traj_read), traj_read[-1].get_potential_energy())
