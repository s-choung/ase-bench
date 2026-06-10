from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Create a Cu FCC bulk 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.5) * (2, 2, 2)
atoms.set_initial_magnetic_moments([0] * len(atoms))

# Set calculator (EMT) and initial velocities
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Langevin MD simulation
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01/units.fs)
dyn.run(100)

# Print initial/final temperature and energy
initial_temp = atoms.get_temperature()
final_temp = dyn.get_temperature()
initial_energy = atoms.get_potential_energy()
final_energy = atoms.get_potential_energy()
print(f"Initial Temperature: {initial_temp:.2f} K")
print(f"Final Temperature: {final_temp:.2f} K")
print(f"Initial Energy: {initial_energy:.2f} eV")
print(f"Final Energy: {final_energy:.2f} eV")
