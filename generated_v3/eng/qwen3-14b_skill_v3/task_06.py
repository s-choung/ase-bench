from ase import Atoms, bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

initial_energy = atoms.get_potential_energy()
initial_temp = atoms.get_temperature()

Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs).run(100)

final_energy = atoms.get_potential_energy()
final_temp = atoms.get_temperature()

print(f"Initial Temperature: {initial_temp:.2f} K, Initial Energy: {initial_energy:.2f} eV")
print(f"Final Temperature: {final_temp:.2f} K, Final Energy: {final_energy:.2f} eV")
