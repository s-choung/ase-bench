from ase.build import bulk
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.calculators.emt import EMT
from ase import units

# Create a Cu FCC 2x2x2 supercell
atoms = bulk('Cu', crystalstructure='fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()  # Set EMT calculator

# Set up Langevin dynamics
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.002)

# Initialize velocities based on Maxwell-Boltzmann distribution
MaxwellBoltzmannDistribution(atoms, 300)
Stationary(atoms)  # Remove center-of-mass motion

# Run Langevin MD with temperature ramp
steps = 200
initial_temperature = 300
final_temperature = 600
temperature_ramp = (final_temperature - initial_temperature) / steps

for i in range(steps):
    dyn.run(50)  # Run Langevin MD for 50 steps
    
    # Print current iteration and temperature every 50 steps
    print(f"Iteration {i+1}, Temperature: {atoms.get_temperature():.2f} K")
    
    # Adjust temperature every 50 steps
    dyn.set_temperature(initial_temperature + (i+1) * temperature_ramp)

print("MD run completed.")
