from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, 5*units.fs, temperature_K=300, friction=0.01/units.fs, trajectory='traj.traj')
dyn.run(10)

frames = read('traj.traj', index=':')
print(len(frames))
print(frames[-1].get_potential_energy())
