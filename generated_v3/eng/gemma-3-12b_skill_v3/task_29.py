from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.calculators.emt import EMT
import numpy as np
from ase import units

atoms = bulk('Pd', 'fcc', a=3.92, supercell=(2, 2, 2))
atoms.calc = EMT()

# Set initial temperature
MaxwellBoltzmannDistribution = ase.md.velocitydistribution.MaxwellBoltzmannDistribution
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# NVE dynamics
md = VelocityVerlet(atoms, timestep=2 * units.fs)

# Initial energy
initial_energy = atoms.get_potential_energy() + sum([a.get_kinetic_energy() for a in atoms])

# Run MD
md.run(200)

# Final energy
final_energy = atoms.get_potential_energy() + sum([a.get_kinetic_energy() for a in atoms])

# Calculate energy difference
energy_diff = final_energy - initial_energy

print(f"Energy difference: {energy_diff}")
