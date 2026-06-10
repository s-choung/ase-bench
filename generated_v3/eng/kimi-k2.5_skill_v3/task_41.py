from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import read
from ase import units

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

VelocityVerlet(atoms, 5*units.fs, trajectory='md.traj').run(10)

traj = read('md.traj', index=':')
print(len(traj))
traj[-1].calc = EMT()
print(traj[-1].get_potential_energy())
