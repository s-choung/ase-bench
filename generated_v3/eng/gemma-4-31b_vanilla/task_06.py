import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase import units

# Setup system
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

# MD Parameters
temperature = 300
timestep = 5 * units.fs
steps = 100
friction = 0.01

# Initial state
print(f"Initial Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Initial Temp: {atoms.get_temperature():.2f} K")

# Langevin Dynamics
dyn = Langevin(atoms, timestep, temperature_K=temperature, friction=friction)

# Run simulation
dyn.run(steps)

# Final state
print(f"Final Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Final Temp: {atoms.get_temperature():.2f} K")
