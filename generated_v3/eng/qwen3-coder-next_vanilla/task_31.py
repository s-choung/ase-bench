from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.units import GPa, kB
from ase.md.nptberendsen import NPTBerendsen
from ase.calculators.emt import EMT
from ase import units

# Create Al FCC 2x2x2 supercell
al = FaceCenteredCubic('Al', size=(2, 2, 2))

# Set up EMT calculator
al.calc = EMT()

# Initial volume
initial_volume = al.get_volume()

# Convert pressure: 10 GPa to eV/Å^3
# 1 eV/Å^3 = 160.21766208 GPa
pressure = 10 * GPa / (160.21766208 * units.eV / units.Ang**3)

# MD parameters
temperature = 500  # K
time_step = 1.0 * units.fs
friction = 0.005   # friction constant for NPTBerendsen

# Set up NPTBerendsen dynamics
dyn = NPTBerendsen(al, time_step, temperature, pressure, 
                   taut=100 * units.fs, taup=1000 * units.fs)

# Run 100 steps
dyn.run(100)

# Final volume
final_volume = al.get_volume()

# Print volumes
print(f"Initial volume: {initial_volume:.4f} Å^3")
print(f"Final volume: {final_volume:.4f} Å^3")
