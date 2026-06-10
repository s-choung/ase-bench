import numpy as np
from ase.build import bulk, EMT
from ase.md.verlet import VelocityVerlet
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase.units import units

# Create a Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6 * units.angstrom, cubic=True)
atoms.calc = EMT()

# Set up NVE MD
md = VelocityVerlet(atoms, timestep=1.0 * units.fs)  # 1 fs timestep
md.run(50)

# Get initial and final energies
initial_energy = atoms.get_potential_energy()
final_energy = atoms.get_potential_energy()

# Print the initial and final energies
print(f"Initial Energy: {initial_energy}")
print(f"Final Energy: {final_energy}")

# Check for energy conservation (within a tolerance)
tolerance = 1e-6
if abs(initial_energy - final_energy) < tolerance:
    print("Energy conservation verified.")
else:
    print("WARNING: Energy conservation not verified.")
