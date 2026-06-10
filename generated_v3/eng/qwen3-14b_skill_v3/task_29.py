from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Pd', 'fcc').repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

initial_total = atoms.get_potential_energy() + atoms.get_kinetic_energy()

integrator = VelocityVerlet(atoms, 2 * units.fs)
integrator.run(200)

final_total = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Energy difference: {final_total - initial_total} eV")
