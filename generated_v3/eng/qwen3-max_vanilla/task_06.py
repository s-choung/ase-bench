from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# Create 2x2x2 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize Langevin dynamics at 300 K
dyn = Langevin(atoms, 5 * units.fs, temperature_K=300, friction=0.002)

# Initial energy and temperature
init_temp = atoms.get_temperature()
init_energy = atoms.get_potential_energy()

# Run 100 steps
dyn.run(100)

# Final energy and temperature
final_temp = atoms.get_temperature()
final_energy = atoms.get_potential_energy()

print(f"Initial temperature: {init_temp:.2f} K")
print(f"Final temperature: {final_temp:.2f} K")
print(f"Initial energy: {init_energy:.6f} eV")
print(f"Final energy: {final_energy:.6f} eV")
