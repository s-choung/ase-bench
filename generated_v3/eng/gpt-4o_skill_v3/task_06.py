from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

initial_temperature = atoms.get_temperature()
initial_energy = atoms.get_potential_energy()

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
dyn.run(100)

final_temperature = atoms.get_temperature()
final_energy = atoms.get_potential_energy()

print(f"Initial Temperature: {initial_temperature} K")
print(f"Initial Energy: {initial_energy} eV")
print(f"Final Temperature: {final_temperature} K")
print(f"Final Energy: {final_energy} eV")
