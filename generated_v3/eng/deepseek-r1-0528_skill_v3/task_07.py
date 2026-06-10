from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Create FCC Cu bulk with 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
atoms.calc = EMT()

# Set initial velocities to 300K and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Get initial total energy
energy_initial = atoms.get_total_energy()

# Run NVE MD
dyn = VelocityVerlet(atoms, timestep=5*units.fs)
dyn.run(50)

# Get final total energy
energy_final = atoms.get_total_energy()

# Print energy conservation results
print(f"Initial Total Energy: {energy_initial:.5f} eV")
print(f"Final Total Energy:   {energy_final:.5f} eV")
print(f"Energy Difference:    {energy_final - energy_initial:.8f} eV")
