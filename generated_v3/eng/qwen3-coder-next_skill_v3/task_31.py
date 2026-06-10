from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import numpy as np

# Create Al FCC 2x2x2 supercell
al = bulk('Al', 'fcc', a=4.05)
supercell = al * (2, 2, 2)
supercell.calc = EMT()

# Print initial volume
initial_volume = supercell.get_volume()
print(f"Initial volume: {initial_volume:.2f} Å^3")

# Set initial temperature and pressure
temperature = 500  # K
pressure_gpa = 10  # GPa
pressure_eva3 = pressure_gpa * units.bar * 1e3 / units.eV * (units.Ang**3)  # Convert GPa to eV/Å^3

# Initialize velocities and center-of-mass motion
MaxwellBoltzmannDistribution(supercell, temperature_K=temperature)
Stationary(supercell)

# Set up NPTBerendsen dynamics
timestep = 5 * units.fs
friction = 0.05 / units.fs
npt = NPTBerendsen(
    supercell,
    timestep=timestep,
    temperature_K=temperature,
    pressure=pressure_eva3,
    friction=friction,
   _com="fix",  # Fix center-of-mass motion
)

# Run MD for 100 steps
npt.run(100)

# Print final volume
final_volume = supercell.get_volume()
print(f"Final volume: {final_volume:.2f} Å^3")
