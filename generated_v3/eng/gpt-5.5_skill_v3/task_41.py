from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io.trajectory import Trajectory
from ase.io import read

atoms = bulk("Cu", "fcc", a=3.6, cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

traj = Trajectory("cu_md.traj", "w", atoms)
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.attach(traj.write, interval=1)
dyn.run(10)
traj.close()

frames = read("cu_md.traj", index=":")
last = frames[-1]

print("frames:", len(frames))
print("last_energy_eV:", last.get_potential_energy())
