from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 300.0 * units.kB)

initial_temp = atoms.get_temperature()
initial_energy = atoms.get_potential_energy()

dyn = Langevin(atoms, 5 * units.fs, 300, 0.005)
dyn.run(100)

final_temp = atoms.get_temperature()
final_energy = atoms.get_potential_energy()

print(f"Initial temperature: {initial_temp:.2f} K, Initial energy: {initial_energy:.4f} eV")
print(f"Final temperature: {final_temp:.2f} K, Final energy: {final_energy:.4f} eV")
