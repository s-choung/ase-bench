from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase import units
import numpy as np

# Build Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.615)  # 3.615 Å lattice constant

# Set up calculator and attach to atoms
atoms.calc = EMT()

# Set initial velocities for 300 K
temperature = 300  # K
np.random.seed(42)  # For reproducibility

# Maxwell-Boltzmann distribution
velocities = np.random.normal(0, 1, (len(atoms), 3))
velocities *= np.sqrt(units.kB * temperature / atoms.get_masses().reshape(-1, 1))

# Remove center of mass motion
velocities -= velocities.mean(axis=0)
atoms.set_velocities(velocities)

# Get initial total energy (kinetic + potential)
energy_initial = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Initial total energy: {energy_initial:.6f} eV")

# Setup and run NVE MD for 50 steps
dyn = VelocityVerlet(atoms, 1.0 * units.fs)  # 1 fs timestep
dyn.run(steps=50)

# Get final total energy
energy_final = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Final total energy: {energy_final:.6f} eV")
print(f"Energy drift: {abs(energy_final - energy_initial):.2e} eV")
