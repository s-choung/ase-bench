from ase import Atoms
from ase.build import bulk
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import VelocityVerlet
from ase.calculators.emt import EMT

# Create Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.61)
cu.calc = EMT()

# Set initial temperature
MaxwellBoltzmannDistribution(cu, temperature_K=300)

# Initialize MD
dyn = VelocityVerlet(cu, dt=1 * units.fs, trajectory=None, logfile=None)

# Print initial energy
epot = cu.get_potential_energy()
ekin = cu.get_kinetic_energy()
print(f"Initial Energy: {epot + ekin:.5f} eV")

# Run MD
for step in range(50):
    dyn.run(1)

# Print final energy
epot = cu.get_potential_energy()
ekin = cu.get_kinetic_energy()
print(f"Final Energy: {epot + ekin:.5f} eV")
