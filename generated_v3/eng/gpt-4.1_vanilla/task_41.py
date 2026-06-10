from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io import Trajectory

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 300)

trajfile = 'md.traj'
dyn = VelocityVerlet(atoms, 1.0)
traj = Trajectory(trajfile, 'w', atoms)

for i in range(10):
    dyn.run(1)
    traj.write(atoms)
traj.close()

frames = list(Trajectory(trajfile))
print('Total frames:', len(frames))
print('Last frame energy:', frames[-1].get_potential_energy())
