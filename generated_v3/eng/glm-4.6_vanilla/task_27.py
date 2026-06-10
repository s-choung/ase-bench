from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import MDLogger
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.nvtberendsen import NVTBerendsen
import numpy as np

# Create Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09).repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities at 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Set up NVT dynamics with Bussi-like thermostat (using Berendsen as approximation)
dyn = NVTBerendsen(atoms, timestep=5.0*1e-3, temperature_K=500, taut=100.0, trajectory='md.traj')

# Print temperature every 50 steps
def print_temperature():
    if dyn.get_number_of_steps() % 50 == 0:
        temp = atoms.get_temperature()
        print(f"Step {dyn.get_number_of_steps()}: Temperature = {temp:.2f} K")

dyn.attach(print_temperature, interval=1)

# Run MD for 200 steps
dyn.run(200)
