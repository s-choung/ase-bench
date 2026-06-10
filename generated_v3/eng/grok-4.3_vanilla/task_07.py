from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
atoms = bulk('Cu', 'fcc', a=3.58, cubic=True).repeat((2,2,2))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
print(atoms.get_potential_energy() + atoms.get_kinetic_energy())
dyn = VelocityVerlet(atoms, timestep=5*units.fs)
dyn.run(50)
print(atoms.get_potential_energy() + atoms.get_kinetic_energy())
