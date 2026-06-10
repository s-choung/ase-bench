from ase import Atoms
from ase.build import bulk
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import ase.units as units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

initial_temperature = 0.0
initial_energy = atoms.get_potential_energy()
print(f"Initial Temperature: {initial_temperature} K")
print(f"Initial Energy: {initial_energy} eV")

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

md = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
md.run(100)

final_temperature = atoms.get_temperature()
final_energy = atoms.get_potential_energy()
print(f"Final Temperature: {final_temperature} K")
print(f"Final Energy: {final_energy} eV")
