from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create 2x2x2 supercell of Cu FCC
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities for 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Store initial state
initial_temp = atoms.get_temperature()
initial_energy = atoms.get_potential_energy()

# Run Langevin MD at 300K for 100 steps
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
dyn.run(100)

# Store final state
final_temp = atoms.get_temperature()
final_energy = atoms.get_potential_energy()

# Output results
print(f"Initial temperature: {initial_temp:.2f} K")
print(f"Initial energy: {initial_energy:.4f} eV")
print(f"Final temperature: {final_temp:.2f} K")
print(f"Final energy: {final_energy:.4f} eV")
