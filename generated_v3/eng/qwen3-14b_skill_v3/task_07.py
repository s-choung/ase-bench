from ase import Atoms, bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

md = VelocityVerlet(atoms, timestep=5*units.fs)
initial = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Initial energy: {initial:.2f} eV")

md.run(50)
final = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Final energy: {final:.2f} eV")
