from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.615)
cu.calc = EMT()

# Initial 300K velocities
MaxwellBoltzmannDistribution(cu, temperature_K=300)

# Initial total energy
initial_total = cu.get_kinetic_energy() + cu.get_potential_energy()

# NVE MD (1 fs timestep, 50 steps)
dyn = VelocityVerlet(cu, timestep=1e-15)
dyn.run(50)

# Final total energy
final_total = cu.get_kinetic_energy() + cu.get_potential_energy()

# Print conservation check
print(f'Initial total energy: {initial_total:.6f} eV')
print(f'Final total energy:   {final_total:.6f} eV')
