from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build Cu FCC 2x2x2 supercell
cu = bulk('Cu', 'fcc').repeat((2,2,2))
cu.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(cu, temperature_K=300)
Stationary(cu)

# Get initial properties
initial_temp = cu.get_temperature()
initial_energy = cu.get_potential_energy()

# Run Langevin MD
md = Langevin(cu, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
md.run(steps=100)

# Get final properties
final_temp = cu.get_temperature()
final_energy = cu.get_potential_energy()

# Print results
print(f"Initial T: {initial_temp:.2f} K, Initial E: {initial_energy:.2f} eV")
print(f"Final T: {final_temp:.2f} K, Final E: {final_energy:.2f} eV")
