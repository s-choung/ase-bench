from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io.trajectory import Trajectory
from ase.io import read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

traj = Trajectory('cu_md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, timestep=5 * units.fs)
dyn.attach(traj.write, interval=1)
dyn.run(10)
traj.close()

frames = read('cu_md.traj', index=':')
print(f"총 프레임 수: {len(frames)}")
print(f"마지막 프레임 에너지: {frames[-1].get_potential_energy():.6f} eV")
