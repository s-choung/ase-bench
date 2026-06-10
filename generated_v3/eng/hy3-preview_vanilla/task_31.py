from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
import numpy as np

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Convert 10 GPa to eV/Å^3 (1 GPa = 0.0062415 eV/Å^3)
pressure_eV = 10 * 0.0062415

# Initialize NPT Berendsen
dyn = NPTBerendsen(atoms, 
                                 timestep=1.0 * units.fs,
                                 temperature=500 * units.kB,
                                 pressure=pressure_eV,
                                 taut=100 * units.fs,
                                 taup=100 * units.fs)

# Store initial volume
initial_volume = atoms.get_volume()

# Run MD
dyn.run(100)

# Get final volume
final_volume = atoms.get_volume()

print(f"Initial volume: {initial_volume:.2f} Å^3")
print(f"Final volume: {final_volume:.2f} Å^3")
