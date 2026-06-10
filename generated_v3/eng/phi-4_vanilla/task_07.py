from ase import Atoms
from ase.build import bulk
from ase.md.velocitydistribution import maxwell
from ase.md import VelocityVerlet

# Create a copper FCC bulk
cu_fcc = bulk('Cu', 'fcc', 3, 3, 3)

# Set initial temperature and allocate velocities
cu_fcc.set_temperature(300 * 0.1)
maxwell(cu_fcc, 300 * 0.1)

# Define the simulation
dyn = VelocityVerlet(cu_fcc)

# Run the simulation for 50 steps
energy_initial = cu_fcc.get_potential_energy() + cu_fcc.get_kinetic_energy()
dyn.run(50, properties=('energy'))
energy_final = cu_fcc.get_potential_energy() + cu_fcc.get_kinetic_energy()

# Print the total energy at the initial and final steps
print(f"Initial Total Energy: {energy_initial}")
print(f"Final Total Energy: {energy_final}")
