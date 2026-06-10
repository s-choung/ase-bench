from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io import Trajectory
from ase import units

atoms = bulk("Cu", "fcc", a=3.6, cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

trajfile = "cu_md.traj"
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs, trajectory=trajfile, logfile=None)
dyn.run(10)

traj = Trajectory(trajfile)
last = traj[-1]

print("Frames:", len(traj))
print("Last frame energy:", last.get_total_energy())
