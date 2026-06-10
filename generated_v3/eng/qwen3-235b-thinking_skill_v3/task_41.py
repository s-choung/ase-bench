from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io import Trajectory, read
from ase.md import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

traj = Trajectory('md.traj', 'w', atoms)
traj.write(atoms)
md = VelocityVerlet(atoms, timestep=1*units.fs, trajectory=traj)
md.run(10)
traj.close()

frames = read('md.traj', index=':')
print(len(frames))
print(frames[-1].get_potential_energy())
