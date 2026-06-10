from ase import Atoms
from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
from ase.calculators.emt import EMT

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.89).repeat((2,2,2))
atoms.calc = EMT()

# Set initial velocities for 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)  # Remove COM motion

# Record initial energy
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Run VelocityVerlet NVE
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

# Output energy difference
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Total energy difference: {final_energy - initial_energy:.6f} eV")
