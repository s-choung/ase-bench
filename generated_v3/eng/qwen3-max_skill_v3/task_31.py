from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
import numpy as np

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# Convert 10 GPa to eV/Å^3
pressure = 10 * units.GPa

# Initial volume
initial_volume = atoms.get_volume()

# Run NPT MD
md = NPTBerendsen(atoms, timestep=1.0*units.fs, temperature_K=500,
                  pressure=pressure, ttime=1000*units.fs, pfactor=1000*units.fs)
md.run(100)

# Final volume
final_volume = atoms.get_volume()

print(f"Initial volume: {initial_volume:.3f} Å³")
print(f"Final volume: {final_volume:.3f} Å³")
