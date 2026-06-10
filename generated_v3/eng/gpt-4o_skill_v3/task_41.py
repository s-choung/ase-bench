from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory
from ase.io import read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = VelocityVerlet(atoms, timestep=5 * units.fs)

traj = Trajectory('md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)

traj_read = read('md.traj', index=':')

print(f"Total number of frames: {len(traj_read)}")
print(f"Energy of last frame: {traj_read[-1].get_potential_energy()} eV")
