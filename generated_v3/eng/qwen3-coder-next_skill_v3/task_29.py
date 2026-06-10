from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet
from ase import units
import numpy as np

# Create Pd FCC bulk and 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.92) * (2, 2, 2)
atoms.calc = EMT()

# Set initial temperature and remove COM motion
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Save initial total energy
initial_energy = atoms.get_total_energy()

# Run NVE MD
timestep = 2 * units.fs
md = VelocityVerlet(atoms, timestep=timestep)
md.run(200)

# Save final total energy
final_energy = atoms.get_total_energy()

# Print energy difference
print(f"Energy difference: {final_energy - initial_energy:.6f} eV")
