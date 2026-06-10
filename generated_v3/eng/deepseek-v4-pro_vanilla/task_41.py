from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io import Trajectory, read
from ase import units

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
traj = Trajectory('cu_md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)
traj.close()

frames = read('cu_md.traj', index=':')
print('Number of frames:', len(frames))
print('Energy of last frame:', frames[-1].get_potential_energy())
