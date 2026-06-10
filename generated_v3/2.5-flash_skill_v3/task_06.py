from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

initial_temp = atoms.get_temperature()
initial_energy = atoms.get_potential_energy()

md = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
md.run(100)

final_temp = atoms.get_temperature()
final_energy = atoms.get_potential_energy()

print(f"Initial Temperature: {initial_temp:.2f} K")
print(f"Initial Potential Energy: {initial_energy:.2f} eV")
print(f"Final Temperature: {final_temp:.2f} K")
print(f"Final Potential Energy: {final_energy:.2f} eV")
