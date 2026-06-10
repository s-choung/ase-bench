from ase import Atoms, bulk, units
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', 'fcc', a=3.615) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

initial_temp = atoms.get_temperature()
initial_energy = atoms.get_total_energy()

dyn = Langevin(atoms, 5 * units.fs, 300, friction=1e-4)
dyn.run(100)

final_temp = atoms.get_temperature()
final_energy = atoms.get_total_energy()

print(f"Initial temperature: {initial_temp:.1f} K")
print(f"Final temperature: {final_temp:.1f} K")
print(f"Initial total energy: {initial_energy:.3f} eV")
print(f"Final total energy: {final_energy:.3f} eV")
