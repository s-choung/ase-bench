from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet

atoms = bulk('Pd', 'fcc') * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
e0 = atoms.get_kinetic_energy() + atoms.get_potential_energy()
dyn = VelocityVerlet(atoms, timestep=2*units.fs)
dyn.run(200)
e1 = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f'{e1 - e0:.6e}')
