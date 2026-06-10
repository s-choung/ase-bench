from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.langevin import Langevin
from ase.io import Trajectory, read

atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

dyn = Langevin(atoms, 1.0, temperature_K=300, timestep=1.0, friction=0.01)
traj = Trajectory('md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)

frames = read('md.traj', index=':')
print(f"Frames: {len(frames)}")
print(f"Last energy: {frames[-1].get_potential_energy()}")
