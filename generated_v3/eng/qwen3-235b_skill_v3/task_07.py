from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
dyn = VelocityVerlet(atoms, timestep=5 * units.fs)
dyn.run(50)
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial energy: {initial_energy:.6f} eV")
print(f"Final energy: {final_energy:.6f} eV")
