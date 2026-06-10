from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
md = VelocityVerlet(atoms, timestep=5*units.fs, trajectory='md.traj')
md.run(10)
traj = read('md.traj', index=':')
print(len(traj))
print(traj[-1].get_potential_energy())
