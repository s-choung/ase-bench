from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import fs, K, eV

# Create and set up the Cu FCC 2x2x2 supercell
atoms = Atoms('Cu64', cell=[[4.05, 0, 0], [0, 4.05, 0], [0, 0, 4.05]], pbc=True)
atoms.set_calculator(EMT())

# Print initial temperature and energy
initial_energy = atoms.get_potential_energy()
initial_temp = atoms.get_temperature()
print(f"Initial Temperature: {initial_temp:.2f} K")
print(f"Initial Energy: {initial_energy:.6f} eV")

# Set up the Langevin thermostat MD
timestep = 5 * fs
temp = 300 * K
friction = 0.01
dyn = Langevin(atoms, timestep, temp, friction)

# Run 100 steps
dyn.run(100)

# Print final temperature and energy
final_energy = atoms.get_potential_energy()
final_temp = atoms.get_temperature()
print(f"Final Temperature: {final_temp:.2f} K")
print(f"Final Energy: {final_energy:.6f} eV")
