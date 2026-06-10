from ase import Atoms
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.calculators.emt import EMT
from ase.units import fs

# Create Cu FCC bulk
atoms = Atoms('Cu4', positions=[[0, 0, 0], [0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]],
              cell=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], pbc=True)
atoms.calc = EMT()

# Set initial temperature
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Store initial energy
initial_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()

# Setup and run MD
dyn = VelocityVerlet(atoms, timestep=1*fs)
for step in range(50):
    dyn.run(1)

# Get final energy
final_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()

print(f'Initial total energy: {initial_energy:.6f} eV')
print(f'Final total energy: {final_energy:.6f} eV')
print(f'Energy difference: {final_energy-initial_energy:.6e} eV')
