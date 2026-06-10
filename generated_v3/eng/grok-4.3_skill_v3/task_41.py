from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io.trajectory import Trajectory
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
dyn = VelocityVerlet(atoms, 5*units.fs, trajectory='traj.traj')
dyn.run(10)
traj = Trajectory('traj.traj')
print(len(traj), traj[-1].get_potential_energy())
