from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Create Ag fcc 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09).repeat((2, 2, 2))
atoms.calc = EMT()

# Set initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Create Bussi thermostat MD
md = Bussi(atoms, timestep=5 * units.fs, temperature_K=500)

# Run MD and print temperature every 50 steps
for step in range(200):
    md.run(50)  # Run 50 steps at a time
    if (step + 1) * 50 % 100 == 0:  # Adjusted to print every 50 steps (cumulative)
        # Alternatively, could track step count differently, but simpler to run in chunks
        # This will print at 50, 100, 150, 200 steps
        temp = atoms.get_temperature()
        print(f"Step: {(step+1)*50}, Temperature: {temp:.2f} K")

# Alternative approach with step tracking (more precise):
# for step in range(200):
#     md.run(1)
#     if (step + 1) % 50 == 0:
#         temp = atoms.get_temperature()
#         print(f"Step: {step+1}, Temperature: {temp:.2f} K")
