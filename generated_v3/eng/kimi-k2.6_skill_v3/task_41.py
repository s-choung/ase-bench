from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io import read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
VelocityVerlet(atoms, 5 * units.fs, trajectory='md.traj').run(10)

traj = read('md.traj', index=':')
print(len(traj))
print(traj[-1].get_potential_energy())
