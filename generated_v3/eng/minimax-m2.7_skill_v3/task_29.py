from ase.build import bulk
from ase import units
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.calculators.emt import EMT

atoms = bulk('Pd', 'fcc', a=3.89).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

E_initial = atoms.get_potential_energy() + atoms.get_kinetic_energy()

VelocityVerlet(atoms, timestep=2*units.fs).run(200)

E_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {E_initial:.6f} eV")
print(f"Final total energy: {E_final:.6f} eV")
print(f"Energy difference: {E_final - E_initial:.6f} eV")
