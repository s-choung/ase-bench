from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.89, cubic=True).repeat((2, 2, 2))

# Set EMT calculator
atoms.calc = EMT()

# Initialize velocities at 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Initialize MD
dyn = VelocityVerlet(atoms, 2.0 * units.fs)

# Record initial total energy
e_start = atoms.get_total_energy()

# Run 200 steps
dyn.run(200)

# Record final total energy
e_end = atoms.get_total_energy()

# Print energy difference
print(f"Energy difference: {e_end - e_start:.6f} eV")
