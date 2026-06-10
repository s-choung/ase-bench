from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import Langevin
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Create Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities to 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300.0)

# Get initial properties
init_pot = atoms.get_potential_energy()
init_temp = atoms.get_temperature()

# Setup and run Langevin MD
dyn = Langevin(atoms, timestep=5.0 * units.fs, temperature_K=300.0, friction=0.01)
dyn.run(100)

# Get final properties
fin_pot = atoms.get_potential_energy()
fin_temp = atoms.get_temperature()

# Print results
print(f"Initial Temperature: {init_temp:.2f} K")
print(f"Initial Energy: {init_pot:.3f} eV")
print(f"Final Temperature: {fin_temp:.2f} K")
print(f"Final Energy: {fin_pot:.3f} eV")
