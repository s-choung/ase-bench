import ase
from ase import Atoms
from ase.io import read, write
from ase.units import GPa
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.calculators.emt import EMT
import numpy as np

# Create FCC Al 2x2x2 supercell
alat = 4.05  # Lattice constant for Al in Å
cell = alat * np.eye(3)
fcc = Atoms('Al', cell=cell, scaled_positions=[(0, 0, 0)], pbc=True)
supercell = fcc * (2, 2, 2)

# Setup calculator
supercell.calc = EMT()

# Set up NPT Berendsen MD
temperature = 500.0  # K
pressure_gpa = 10.0  # GPa
pressure_ev_per_ang3 = pressure_gpa * GPa  # Convert to eV/Å^3

# Initialize velocities
MaxwellBoltzmannDistribution(supercell, temperature_K=temperature)

# Create NPT dynamics
timestep = 5.0  # fs
ttime = 100.0  # fs
ptime = 100.0  # fs
dyn = NPTBerendsen(supercell, timestep=timestep, temperature_K=temperature,
                   pressure_au=pressure_ev_per_ang3, 
                   taut=ttime, taup=ptime)

# Print initial volume
print(f"Initial volume: {supercell.get_volume():.3f} Å^3")

# Run 100 MD steps
for i in range(100):
    dyn.run(1)

# Print final volume
print(f"Final volume: {supercell.get_volume():.3f} Å^3")
