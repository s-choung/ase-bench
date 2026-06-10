from ase import units
from ase.build import bulk
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import VelocityVerlet
from ase.calculators.emt import EMT

atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
e_start = atoms.get_potential_energy() + atoms.get_kinetic_energy()
dyn = VelocityVerlet(atoms, timestep=2.0 * units.fs)
dyn.run(200)
e_end = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(e_end - e_start)
