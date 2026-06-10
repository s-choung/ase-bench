from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Create 3x3x3 FCC Cu bulk supercell
atoms = bulk('Cu', 'fcc', a=3.615).repeat((3, 3, 3))
atoms.calc = EMT()

# Initialize 300K velocity distribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Calculate initial total energy
initial_ekin = atoms.get_kinetic_energy()
initial_epot = atoms.get_potential_energy()
initial_etot = initial_ekin + initial_epot

# Set up NVE Velocity Verlet MD (1 fs timestep, 50 steps)
dyn = VelocityVerlet(atoms, timestep=1*units.fs)
dyn.run(50)

# Calculate final total energy
final_ekin = atoms.get_kinetic_energy()
final_epot = atoms.get_potential_energy()
final_etot = final_ekin + final_epot

# Print energies to verify conservation
print(f"Initial total energy: {initial_etot:.3f} eV")
print(f"Final total energy:   {final_etot:.3f} eV")
