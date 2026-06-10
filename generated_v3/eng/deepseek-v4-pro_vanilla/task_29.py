from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet

# Build Pd FCC 2x2x2 supercell (lattice constant approx. 3.89 Å)
atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)

# Attach an EMT calculator
atoms.calc = EMT()

# Initialize velocities at 500 K and remove total momentum
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Total energy before dynamics
E_start = atoms.get_kinetic_energy() + atoms.get_potential_energy()

# NVE dynamics with Velocity-Verlet, 2 fs timestep, 200 steps
dyn = VelocityVerlet(atoms, timestep=2.0)  # dt in ASE time units (fs)
dyn.run(200)

# Total energy after dynamics
E_end = atoms.get_kinetic_energy() + atoms.get_potential_energy()

# Print difference
print(E_end - E_start)
