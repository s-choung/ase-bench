from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Pd', 'fcc') * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

initial_kinetic = atoms.get_kinetic_energy()
initial_potential = atoms.get_potential_energy()
initial_total = initial_kinetic + initial_potential

VelocityVerlet(atoms, 2 * units.fs).run(200)

final_kinetic = atoms.get_kinetic_energy()
final_potential = atoms.get_potential_energy()
final_total = final_kinetic + final_potential

print(f"Total energy difference: {abs(final_total - initial_total):.6f} eV")
