from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.velocityverlet import VelocityVerlet

# Cu FCC bulk (2x2x2 supercell)
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Set temperature to 300 K and zero total momentum
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
atoms.set_momenta(atoms.get_momenta() - atoms.get_momenta().mean(axis=0))

# Initial energy
ekin0 = atoms.get_kinetic_energy()
epot0 = atoms.get_potential_energy()
print(f'Initial total energy: {ekin0 + epot0:.6f} eV '
      f'(Ekin={ekin0:.6f}, Epot={epot0:.6f})')

# NVE MD (VelocityVerlet) for 50 steps
dyn = VelocityVerlet(atoms, dt=1 * units.fs)
for _ in range(50):
    dyn.run(1)

# Final energy
ekin1 = atoms.get_kinetic_energy()
epot1 = atoms.get_potential_energy()
print(f'Final total energy:   {ekin1 + epot1:.6f} eV '
      f'(Ekin={ekin1:.6f}, Epot={epot1:.6f})')
