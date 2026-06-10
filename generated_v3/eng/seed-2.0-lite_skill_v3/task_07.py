from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build 2x2x2 supercell of FCC Cu bulk
atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
atoms = atoms * (2, 2, 2)

# Assign built-in EMT calculator
atoms.calc = EMT()

# Initialize 300K Maxwell-Boltzmann velocities, remove center-of-mass drift
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Calculate and print initial total energy (kinetic + potential)
initial_total = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy: {initial_total:.4f} eV")

# Set up and run NVE (VelocityVerlet) MD for 50 steps
dyn = VelocityVerlet(atoms, timestep=1*units.fs)
dyn.run(50)

# Calculate and print final total energy
final_total = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final total energy:   {final_total:.4f} eV")
print(f"Energy difference:    {abs(final_total - initial_total):.6f} eV")
