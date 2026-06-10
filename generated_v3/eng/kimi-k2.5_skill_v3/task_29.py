from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Pd', 'fcc', a=3.96) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

e_init = atoms.get_potential_energy() + atoms.get_kinetic_energy()

vv = VelocityVerlet(atoms, timestep=2*units.fs)
vv.run(200)

e_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(e_final - e_init)
