from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io import Trajectory, read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

trajfile = 'cu_md.traj'
dyn = VelocityVerlet(atoms, timestep=1 * units.fs, trajectory=trajfile, logfile=None)
dyn.run(10)

traj = read(trajfile, index=':')
print(len(traj), traj[-1].get_potential_energy() + traj[-1].get_kinetic_energy())
