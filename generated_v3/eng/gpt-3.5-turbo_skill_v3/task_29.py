from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', crystalstructure='fcc', a=3.89) * (2, 2, 2)
atoms.set_calculator(EMT())

# Set initial temperature to 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Remove center of mass motion
Stationary(atoms)

# Run VelocityVerlet NVE MD for 200 steps with a timestep of 2 fs
dyn = VelocityVerlet(atoms, timestep=2*units.fs)
dyn.run(200)

# Calculate the difference in total energy
initial_energy = atoms.get_total_energy()
final_energy = atoms.get_total_energy()
energy_difference = final_energy - initial_energy
print(f"Total energy difference: {energy_difference} eV")
