from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import ase.units as units

# Create Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()

# Initialize velocities (300K, remove COM drift)
MaxwellBoltzmannDistribution(cu, temperature_K=300)
Stationary(cu)

# Initial total energy (kinetic + potential)
initial_total = cu.get_kinetic_energy() + cu.get_potential_energy()

# NVE MD (VelocityVerlet) for 50 steps
md = VelocityVerlet(cu, timestep=5*units.fs)
md.run(steps=50)

# Final total energy
final_total = cu.get_kinetic_energy() + cu.get_potential_energy()

# Print energy conservation check
print(f'Initial total energy (eV): {initial_total:.6f}')
print(f'Final total energy (eV): {final_total:.6f}')
