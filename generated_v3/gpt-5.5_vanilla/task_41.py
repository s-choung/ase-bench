from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io.trajectory import Trajectory
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Cu", "fcc", a=3.6, cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)

traj_file = "cu_md.traj"
with Trajectory(traj_file, "w", atoms) as traj:
    for _ in range(10):
        dyn.run(1)
        traj.write(atoms)

traj = Trajectory(traj_file, "r")
print("frames:", len(traj))
print("last_energy:", traj[-1].get_potential_energy())
traj.close()
