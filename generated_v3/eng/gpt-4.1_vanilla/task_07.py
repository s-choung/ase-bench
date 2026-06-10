from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Build Cu bulk and attach EMT calculator
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

# Set initial velocities at 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Function to compute total energy
def total_energy(a):
    return a.get_potential_energy() + a.get_kinetic_energy()

print(f'Initial total energy: {total_energy(atoms):.6f} eV')

# Set up and run MD
dyn = VelocityVerlet(atoms, dt=1.0 * units.fs)

for i in range(50):
    dyn.run(1)

print(f'Final total energy:   {total_energy(atoms):.6f} eV')
