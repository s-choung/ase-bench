from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import ase.units as units

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Set initial temperature to 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Initial total energy
initial_energy = atoms.get_total_energy()

# Run NVE MD for 50 steps
md = VelocityVerlet(atoms, timestep=5*units.fs)
md.run(50)

# Final total energy
final_energy = atoms.get_total_energy()

# Print energies
print(f"Initial total energy: {initial_energy:.6f} eV")
print(f"Final total energy:   {final_energy:.6f} eV")
