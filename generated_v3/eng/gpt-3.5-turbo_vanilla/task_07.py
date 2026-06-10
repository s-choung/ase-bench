from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet

# Create Cu FCC bulk
atoms = Atoms('Cu4', positions=[(0, 0, 0), (0, 0.5, 0.5), (0.5, 0, 0.5), (0.5, 0.5, 0)],
              cell=(3, 3, 3), pbc=True)

# Set initial temperature
MaxwellBoltzmannDistribution(atoms, 300)

# Set calculator
atoms.set_calculator(EMT())

# Create VelocityVerlet simulation
dyn = VelocityVerlet(atoms, timestep=1.0)

# Print initial total energy
print('Initial total energy:', atoms.get_potential_energy() + atoms.get_kinetic_energy())

# Run MD for 50 steps
for step in range(50):
    dyn.run(1)

# Print final total energy
print('Final total energy:', atoms.get_potential_energy() + atoms.get_kinetic_energy())
