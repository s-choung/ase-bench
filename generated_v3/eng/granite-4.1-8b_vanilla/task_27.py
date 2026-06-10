from ase import Atoms
from ase.calculators.emt import EMT
from ase.md import Langevin, MartynovBaspovski
from ase import units
import numpy as np

# Create Ag FCC 2x2x2 supercell
ag_fcc = Atoms('Ag', positions=[[0, 0, 0]])
ag_fcc.set_cell([[1, 0, 0], [0, 1, 0], [0, 0, 1]], scale_atoms=True)
ag_fcc *= 2

# Set up EMT calculator
calc = EMT()
ag_fcc.set_calculator(calc)

# Initialize Martynov-Baspovski thermostat (Bussi thermostat)
thermostat = MartynovBaspovski(ag_fcc, T=500*units.kB, seed=1)
md = Langevin(ag_fcc, 5.0*units.fs, 500*units.kB, 1.0*units.fs, thermostat=thermostat)

# Run MD
md.run(200)

# Function to print temperature every 50 steps
def print_temperature(atoms, step):
    temperature = atoms.get_temperature()
    print(f"Step {step}: Temperature = {temperature:.2f} K")

# Simulate temperature recording
for step in range(0, 201, 50):
    if step < 200:
        print_temperature(ag_fcc, step)
