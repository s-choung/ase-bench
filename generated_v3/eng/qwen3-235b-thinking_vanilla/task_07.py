from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import VelocityVerlet

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 300 * units.kB)
initial_energy = atoms.get_kinetic_energy() + atoms.get_potential_energy()
dyn = VelocityVerlet(atoms, dt=5.0)
dyn.run(50)
final_energy = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Initial total energy: {initial_energy:.6f} eV")
print(f"Final total energy: {final_energy:.6f} eV")
