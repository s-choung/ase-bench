from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.md import langevin
from ase.calculator.emt import EMT
import numpy as np

# Create Ag 2x2x2 FCC supercell
atoms = FaceCenteredCubic(symbol='Ag', size=(2, 2, 2))
atoms.calc = EMT()

# Set initial temperature (500 K)
MaxwellBoltzmannDistribution(atoms, 500 * 8.617e-5)

# Set up NVT MD with Bussi thermostat (Langevin)
dyn = VelocityVerlet(atoms, timestep=5 * 1e-15)

# Run MD
def print_temp():
    temp = atoms.get_temperature()
    step = dyn.get_number_of_steps()
    if step % 50 == 0:
        print(f"Step {step}: Temperature = {temp:.2f} K")

for i in range(200):
    dyn.run(1)
    print_temp()
    # Apply Bussi thermostat via Langevin (approximated with weak coupling)
    # Using a weak Langevin thermostat to mimic Bussi's method
    if dyn.get_number_of_steps() % 1 == 0:
        langevin.Langevin(atoms, 5 * 1e-15, temperature=500 * 8.617e-5, friction=0.005).step()
