from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import VelocityVerlet
from ase.io import Trajectory

atoms = bulk('Cu')
atoms.set_calculator(EMT())
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
dyn = VelocityVerlet(atoms, dt=1.0)
trajectory = Trajectory('cu_md.traj', 'w', atoms)
dyn.attach(trajectory.write, interval=1)
dyn.run(10)
traj = Trajectory('cu_md.traj')
print(len(traj))
print(traj[-1].get_potential_energy())
