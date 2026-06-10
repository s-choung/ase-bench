from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io import Trajectory, read

atoms = bulk('Cu', cubic=True)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 300 * units.kB)
traj = Trajectory('md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, 1.0 * units.fs)
for _ in range(10):
    dyn.run(1)
    traj.write(atoms)
traj.close()

traj = read('md.traj', ':')
print(len(traj))
print(traj[-1].get_potential_energy())
