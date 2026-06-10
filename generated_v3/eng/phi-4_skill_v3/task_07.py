from ase import Atoms
from ase.build import bulk
from ase.thermo import MaxwellBoltzmannDistribution
from ase.md.velocityverlet import VelocityVerlet
from ase import units

# Step 1: Initialize the bulk structure
atoms = bulk('Cu', 'fcc', a=3.6)

# Step 2: Set initial temperature with a Maxwell-Boltzmann distribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Step 3: Set GEMS calculator to EMT to calculate potential energy
atoms.set_calculator(EMT_calculator)

# Calculate initial total energy
atoms1 = atoms.copy()
initial_potential_energy = atoms1.get_potential_energy()
initial_kinetic_energy = atoms1.get_kinetic_energy()
initial_total_energy = initial_potential_energy + initial_kinetic_energy

# Print the initial total energy
print("Initial Total Energy: ", initial_total_energy)
print("Initial Potential Energy: ", initial_potential_energy)
print("Initial Kinetic Energy: ", initial_kinetic_energy)

# Prepare the MD simulation using Velocity Verlet
md = VelocityVerlet(atoms=atoms, timestep=0.5 * units.fs, trajectory="nve_md.traj")

# Run NVE MD for 50 steps
md.run(steps=50)

# Calculate kinetic and potential energies after the simulation
final_total_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Print the final total energy for verification of energy conservation
print("Final Total Energy: ", final_total_energy)
print("Final Potential Energy: ", atoms.get_potential_energy())
print("Final Kinetic Energy: ", atoms.get_kinetic_energy())
