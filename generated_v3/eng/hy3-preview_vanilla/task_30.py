import ase
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
import numpy as np

# Create 3x3x3 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((3,3,3))
atoms.calc = EMT()

# Store initial volume
initial_volume = atoms.get_volume()

# Initialize NPT Berendsen dynamics
dyn = NPTBerendsen(
    atoms,
    timestep=5*units.fs,
    temperature=300,
    pressure=1e5*units.Pascal,  # 1 bar in Pa
    taut=100*units.fs,
    taup=1000*units.fs
)

# Run MD
dyn.run(200)

# Get final properties
final_volume = atoms.get_volume()
final_pressure = atoms.get_pressure() / (1e5*units.Pascal)  # Convert to bar

# Output results
print(f"Initial cell volume: {initial_volume:.2f} Å³")
print(f"Final cell volume: {final_volume:.2f} Å³")
print(f"Final pressure: {final_pressure:.3f} bar")
