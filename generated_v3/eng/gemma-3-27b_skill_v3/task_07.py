from ase import Atoms
from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import ase.units as units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Run MD
md = VelocityVerlet(atoms, timestep=5 * units.fs)
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
md.run(50)
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {initial_energy:.4f} eV")
print(f"Final total energy: {final_energy:.4f} eV")
