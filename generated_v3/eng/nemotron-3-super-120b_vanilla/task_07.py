from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md import MaxwellBoltzmannDistribution

# Cu FCC bulk (2x2x2 supercell)
atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

# Set temperature to 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300.0)

# Initial total energy
E0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f'Initial total energy: {E0:.6f} eV')

# NVE MD (Velocity Verlet)
dyn = VelocityVerlet(atoms, dt=5*units.fs)
for _ in range(50):
    dyn.run(1)

# Final total energy
Ef = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f'Final total energy: {Ef:.6f} eV')
