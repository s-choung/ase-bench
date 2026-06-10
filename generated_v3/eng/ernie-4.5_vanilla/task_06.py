from ase.build import bulk
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
import numpy as np

# Create FCC copper supercell
atoms = bulk('Cu', 'fcc', cubic=True).repeat(2, 2, 2)

# Set up calculator
atoms.calc = EMT()

# Define parameters for Langevin dynamics
timestep = 5.0  # in fs
temperature = 300  # in K
steps = 100

# Create Langevin dynamics object
dyn = Langevin(atoms, timestep=timestep * 1e-3,  # ASE uses ps as time unit, convert fs to ps
               temperature=temperature,
               friction=0.002,
               logfile=None)

# Print initial temperature and energy
initial_temperature = atoms.get_temperature()  # (This will be 0 currently; to get temp from kinetic energy we need velocities, so alternatively:)
# If you have initialized velocities or after first step, but for initial usually we haven't run, so directly 0 or from set:
# For clearer output, we can calculate initial KE-based temperature setup if needed, but usually 'get_temperature()' uses current velocities
initial_kinetic_energy = atoms.get_kinetic_energy()
# To get a meaningful initial temperature, we'd need to initialize with temperatures, but here we can print as 0 or note no velocity thus 0

print(f"Initial temperature: {initial_temperature} K (based on current velocities, likely 0 if not set)")
print(f"Initial potential energy: {atoms.get_potential_energy():.2f} eV")

# Run MD
dyn.run(steps)

# Print final temperature and energy
final_temperature = atoms.get_temperature()  # Now based on the final velocities
final_kinetic_energy = atoms.get_kinetic_energy()
final_potential_energy = atoms.get_potential_energy()

print(f"Final temperature: {final_temperature:.2f} K")
print(f"Final potential energy: {final_potential_energy:.2f} eV")
