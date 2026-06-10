from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

# Create Cu FCC bulk (3x3x3 supercell)
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((3, 3, 3))
atoms.calc = EMT()

# Initialize velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Print initial total energy
e_initial = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f'Initial total energy: {e_initial:.6f} eV')

# Run NVE MD for 50 steps with 1 fs timestep
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)

# Print final total energy
e_final = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f'Final total energy: {e_final:.6f} eV')
