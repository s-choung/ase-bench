from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
from ase.io import Trajectory

atoms = bulk('Cu', cubic=True)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

dyn = VelocityVerlet(atoms, 5 * units.fs, trajectory='md.traj')
dyn.run(10)

traj = Trajectory('md.traj')
print(len(traj))
print(traj[-1].get_potential_energy())
