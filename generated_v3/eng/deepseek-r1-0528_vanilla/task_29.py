from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Set initial temperature
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Initialize dynamics with 2 fs timestep
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)

# Record initial energy
initial_energy = atoms.get_total_energy()

# Run 200 MD steps
dyn.run(200)

# Calculate and print energy difference
final_energy = atoms.get_total_energy()
print(f"{final_energy - initial_energy:.6f}")
