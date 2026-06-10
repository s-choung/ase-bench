from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.langevin import Langevin
from ase.io import read, Trajectory

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

md = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.02/units.fs)
traj = Trajectory('cu_md.traj', 'w', atoms)
md.attach(traj)
md.run(10)
traj.close()

traj = read('cu_md.traj', index=':')
print(len(traj))
print(traj[-1].get_potential_energy())
