from ase import Atoms
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.calculators.emt import EMT

# Create a Pd FCC 2x2x2 supercell
atoms = Atoms('Pd', positions=[[0, 0, 0]], cell=[[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]], pbc=True)
atoms = atoms.repeat((2, 2, 2))

# Set the calculator
atoms.calc = EMT()

# Set the initial temperature
MaxwellBoltzmannDistribution(atoms, 500 * ase.units.kB)

# Initialize the dynamics
dyn = VelocityVerlet(atoms, timestep=2 * ase.units.fs)

# Store initial total energy
initial_energy = atoms.get_kinetic_energy() + atoms.get_potential_energy()

# Run the dynamics
for _ in range(200):
    dyn.run(1)

# Calculate final total energy
final_energy = atoms.get_kinetic_energy() + atoms.get_potential_energy()

# Print the difference in total energy
print(final_energy - initial_energy)
