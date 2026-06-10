from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.io import Trajectory
import ase.units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

dyn = VelocityVerlet(atoms, timestep=2 * ase.units.fs)
traj = Trajectory('Cu_md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)
traj.close()

traj = Trajectory('Cu_md.traj')
print('Total frames:', len(traj))
print('Energy of last frame (eV):', traj[-1].get_potential_energy())
traj.close()
