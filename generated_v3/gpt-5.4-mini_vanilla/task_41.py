from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io import Trajectory, read
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

traj = Trajectory('cu_md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, timestep=1 * units.fs)
dyn.attach(traj.write, interval=1)

for _ in range(10):
    dyn.run(1)

traj.close()

frames = read('cu_md.traj', ':')
print(len(frames))
print(frames[-1].get_potential_energy())
