from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import (
    MaxwellBoltzmannDistribution,
    Stationary,
    ZeroRotation,
)

# Build Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.615)
atoms.calc = EMT()

# Set initial temperature to 300K and randomize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

# Store initial energy
initial_kinetic = atoms.get_kinetic_energy()
initial_potential = atoms.get_potential_energy()
initial_total = initial_kinetic + initial_potential

print(f"Initial energy:")
print(f"  Kinetic:  {initial_kinetic:.6f} eV")
print(f"  Potential: {initial_potential:.6f} eV")
print(f"  Total:    {initial_total:.6f} eV")

# Run NVE MD for 50 steps
md = VelocityVerlet(atoms, timestep=5.0 * units.fs)
md.run(50)

# Calculate final energy
final_kinetic = atoms.get_kinetic_energy()
final_potential = atoms.get_potential_energy()
final_total = final_kinetic + final_potential

print(f"\nFinal energy:")
print(f"  Kinetic:  {final_kinetic:.6f} eV")
print(f"  Potential: {final_potential:.6f} eV")
print(f"  Total:    {final_total:.6f} eV")

# Energy conservation check
energy_change = abs(final_total - initial_total)
print(f"\nEnergy conservation check:")
print(f"  Initial total: {initial_total:.6f} eV")
print(f"  Final total:   {final_total:.6f} eV")
print(f"  Change:        {energy_change:.6f} eV")
print(f"  Relative change: {energy_change/abs(initial_total)*100:.4f}%")
