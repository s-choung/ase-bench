from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

E_initial = atoms.get_potential_energy() + atoms.get_kinetic_energy()

VelocityVerlet(atoms, timestep=1*units.fs).run(50)

E_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {E_initial:.3f} eV")
print(f"Final total energy: {E_final:.3f} eV")
