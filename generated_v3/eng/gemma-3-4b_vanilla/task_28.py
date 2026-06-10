from ase.md.langevin import Langevin
from ase.md import EMT
from ase.build import fcc111
from ase.calculators import EMT
from ase.io import write
import numpy as np

# Create Cu FCC 2x2x2 supercell
cell = fcc111('Cu', size=(2, 2, 2), shift=True)

# Initialize the system
calc = EMT()
system = cell.set_calculator(calc)

# Set MD parameters
timestep = 5.0
temperature = 300.0
nsteps = 200
dt = timestep

# Langevin MD parameters
langevin = Langevin(
    system,
    velocity=None,
    temperature=temperature,
    timestep=dt,
    viscosity=0.01,
    zeta=0.1,
    random_seed=42
)

# Run MD
for step in range(nsteps):
    langevin.run(nsteps=1)
    if (step + 1) % 50 == 0:
        print(f"Step {step + 1}: Temperature = {system.temperature}")

# Write the final structure
write('cu_langevin.xyz', system)
