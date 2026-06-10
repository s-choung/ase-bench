from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = Atoms('Cu', [(0, 0, 0), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)], cell=(3.6, 3.6, 3.6), pbc=True)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print(f"Initial energy: {atoms.get_kinetic_energy() + atoms.get_potential_energy():.6f} eV")

dyn = VelocityVerlet(atoms, 5.0)
dyn.run(50)

print(f"Final energy: {atoms.get_kinetic_energy() + atoms.get_potential_energy():.6f} eV")
