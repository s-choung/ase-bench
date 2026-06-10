from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase import units
from ase.io.trajectory import Trajectory

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
dyn = VelocityVerlet(atoms, timestep=1*units.fs)
traj = Trajectory('md.traj', 'w', atoms)
dyn.attach(traj, interval=1)
dyn.run(10)

traj = Trajectory('md.traj')
print(len(traj), traj[-1].get_potential_energy())
