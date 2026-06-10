from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.io import Trajectory
from ase.units import fs

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
atoms.calc = EMT()
dyn = VelocityVerlet(atoms, 0.5 * fs)
traj = Trajectory('Cu_md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)

frames = Trajectory('Cu_md.traj')
print(len(frames))
print(frames[-1].get_potential_energy())
