from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io import read
from ase.io.trajectory import Trajectory
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet

atoms = bulk("Cu", "fcc", a=3.6, cubic=True).repeat((3, 3, 3))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

traj = Trajectory("cu_md.traj", "w", atoms)
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.attach(traj.write, interval=1)
dyn.run(10)
traj.close()

frames = read("cu_md.traj", index=":")
print("frames:", len(frames))
print("last_energy_eV:", frames[-1].get_potential_energy())
