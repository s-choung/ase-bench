from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Pd', 'fcc').repeat((2, 2, 2))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temp_K=500)

e0 = atoms.get_kinetic_energy() + atoms.get_potential_energy()
dyn = VelocityVerlet(atoms, 2 * units.fs, logfile=None)
dyn.run(200)
e1 = atoms.get_kinetic_energy() + atoms.get_potential_energy()

print(e1 - e0)
