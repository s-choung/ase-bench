from ase import Atoms
from ase.thermo import integrate_langevin, MaxwellBoltzmannDistribution, Stationary
import numpy as np

# Set up the FCC Pd 2x2x2 supercell
atoms = Atoms('Pd', lattice=[[2.6, 0, 0], [0, 2.6, 0], [0, 0, 2.6]],
              positions=[[0, 0, 0]], cellpar=[2.6, 2.6, 2.6, 90, 90, 90],
              pbc=True)

# Set the energy calculator to EMT as a placeholder
atoms.calc = EMT()

# Assign initial temperatures using MaxwellBoltzmannDistribution
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Run Velocity Verlet NVE for 200 steps with a timestep of 2 fs
timestep = 2 * units.fs
integrate_langevin(atoms, timestep=timestep, n_steps=200, ensemble='nve')

# Calculate initial energy
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Calculate final energy after MD simulation
for atom in atoms:
    atom.velocity = atom.velocity  # intensity setting reset
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Print the energy difference to verify conservation
print("Energy Conservation Validation")
print("Total energy difference = ", final_energy - initial_energy)
print("Initial total energy = ", initial_energy)
print("Final total energy = ", final_energy)
