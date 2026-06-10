from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet

# Create 2x2x2 FCC Pd supercell
pd_bulk = bulk('Pd', 'fcc', a=3.89)
atoms = pd_bulk.repeat((2, 2, 2))

# Attach built-in EMT calculator
atoms.calc = EMT()

# Initialize velocities to 500K
atoms.set_temperature(500)

# Set up NVE VelocityVerlet dynamics with 2 fs timestep
dyn = VelocityVerlet(atoms, timestep=2)

# Calculate initial total energy
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Run 200 MD steps
dyn.run(steps=200)

# Calculate final total energy and print difference
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Total energy difference (end - start): {final_energy - initial_energy:.8f} eV")
