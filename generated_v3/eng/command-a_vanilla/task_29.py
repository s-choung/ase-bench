from ase import Atoms
from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.calculators.emt import EMT
import numpy as np

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.88).repeat((2, 2, 2))
atoms.calc = EMT()

# Set initial temperature to 500K
atoms.set_initial_momenta(temperature=500)

# Initialize NVE MD with 2 fs timestep
dyn = VelocityVerlet(atoms, 2 * 0.001)

# Store initial total energy
initial_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()

# Run MD for 200 steps
dyn.run(200)

# Store final total energy
final_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()

# Print energy difference
print(f"Energy difference: {final_energy - initial_energy:.6f} eV")
