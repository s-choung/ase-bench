from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import kJ

# Create copper bulk
cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)

# Assign EMT calculator
cu_bulk.calc = EMT()

# Set initial temperature
MaxwellBoltzmannDistribution(cu_bulk, temperature_K=300)

# Trajectory
dyn = VelocityVerlet(cu_bulk, dt=1.0)

def print_energy(a):
    epot = a.get_potential_energy()
    ekin = a.get_kinetic_energy()
    print(f'Total energy: {epot + ekin:.5f} eV')

# Print initial energy
print("Initial:")
print_energy(cu_bulk)

# Run NVE MD for 50 steps
dyn.run(50)

# Print final energy
print("Final:")
print_energy(cu_bulk)
