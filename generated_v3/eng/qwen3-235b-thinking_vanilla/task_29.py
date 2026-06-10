from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet

atoms = bulk('Pd', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 500 * units.kB)
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
dyn = VelocityVerlet(atoms, 2 * units.fs)
dyn.run(200)
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(final_energy - initial_energy)
