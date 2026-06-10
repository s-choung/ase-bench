from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.io import Trajectory
from ase import units
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
dyn = Langevin(atoms, 5*units.fs, 300, 0.2)
traj = Trajectory('cu.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)
traj.close()
t = Trajectory('cu.traj')
print(len(t), t[-1].get_potential_energy())
