from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io import Trajectory
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import numpy as np

# Build Pd FCC 2x2x2 supercell
atoms = Atoms('Pd', positions=[(0, 0, 0)], cell=[3.95, 3.95, 3.95], pbc=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities at 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)  # Remove center-of-mass motion

# Store initial total energy
initial_energy = atoms.get_total_energy()

# Run VelocityVerlet NVE MD
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

# Calculate energy difference
final_energy = atoms.get_total_energy()
energy_diff = final_energy - initial_energy

print(f"Initial total energy: {initial_energy:.6f} eV")
print(f"Final total energy: {final_energy:.6f} eV")
print(f"Energy difference: {energy_diff:.6e} eV")
print(f"Relative energy change: {abs(energy_diff/initial_energy):.6e}")
