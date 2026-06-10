from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Create a Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

# Set initial temperature to 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Perform NVE MD using VelocityVerlet integrator for 50 steps
dyn = VelocityVerlet(atoms, timestep=5*units.fs)
energies = atoms.get_total_energy()

print(f'Initial total energy: {energies}')
dyn.run(50)
energies = atoms.get_total_energy()
print(f'Final total energy: {energies}')
