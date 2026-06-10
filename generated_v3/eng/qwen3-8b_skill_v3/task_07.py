from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.units import fs

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = VelocityVerlet(atoms, timestep=5 * fs)
dyn.run(50)

initial_total = atoms.get_potential_energy() + atoms.get_kinetic_energy()
final_total = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {initial_total}")
print(f"Final total energy: {final_total}")
