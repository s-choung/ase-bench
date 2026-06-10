from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import fs, kB
import ase.build

# Create bulk Cu FCC 2x2x2 supercell
atoms = ase.build.bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Initial energy and temperature
initial_energy = atoms.get_potential_energy()
initial_temp = atoms.get_temperature()

# Setup Langevin MD
dyn = Langevin(atoms, timestep=5 * fs, temperature_K=300, friction=0.002)

# Run simulation
dyn.run(100)

# Final energy and temperature
final_energy = atoms.get_potential_energy()
final_temp = atoms.get_temperature()

print(f'Initial: T = {initial_temp:.2f} K, E = {initial_energy:.4f} eV')
print(f'Final: T = {final_temp:.2f} K, E = {final_energy:.4f} eV')
