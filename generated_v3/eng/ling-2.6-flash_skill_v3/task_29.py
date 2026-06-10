from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Pd', 'fcc', a=3.89).repeat((2, 2, 2))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

velocities = atoms.get_velocities().copy()

energy_start = atoms.get_kinetic_energy() + atoms.get_potential_energy()

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

energy_end = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f'Energy difference (start - end): {energy_start - energy_end:.6f} eV')
