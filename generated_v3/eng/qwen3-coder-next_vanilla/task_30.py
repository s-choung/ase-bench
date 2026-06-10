from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.nptberendsen import NPTBerendsen
from ase.units import fs, Pa
from ase.calculators.emt import EMT
import numpy as np

# Create Cu FCC 3x3x3 supercell
atoms = FaceCenteredCubic('Cu', size=(3, 3, 3))

# Set up EMT calculator
atoms.calc = EMT()

# Initial properties
initial_volume = atoms.get_volume()
print(f"Initial volume: {initial_volume:.2f} Å^3")

# NPT ensemble parameters
temperature = 300  # K
pressure = 1 * 1e5  # 1 bar in Pa (1 bar = 1e5 Pa)
timestep = 5 * fs
taut = 100 * fs   # Temperature relaxation time
taup = 1000 * fs  # Pressure relaxation time

# Set up NPTBerendsen dynamics
dyn = NPTBerendsen(atoms, timestep, temperature, taut, taup, pressure, fcoupling=0.1)

# Run MD for 200 steps
dyn.run(200)

# Final properties
final_volume = atoms.get_volume()
final_pressure = atoms.get_pressure()
print(f"Final volume: {final_volume:.2f} Å^3")
print(f"Final pressure: {final_pressure/1e5:.2f} bar")
