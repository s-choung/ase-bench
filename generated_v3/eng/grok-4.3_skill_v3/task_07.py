from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
dyn = VelocityVerlet(atoms, timestep=5*units.fs)
print(atoms.get_potential_energy() + atoms.get_kinetic_energy())
dyn.run(50)
print(atoms.get_potential_energy() + atoms.get_kinetic_energy())
