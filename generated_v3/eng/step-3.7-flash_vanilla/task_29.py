from ase.build import fcc
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = fcc('Pd', size=(2, 2, 2))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
E0 = atoms.get_kinetic_energy() + atoms.get_potential_energy()
dyn = VelocityVerlet(atoms, dt=2.0)
dyn.run(200)
Ef = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Energy difference: {Ef - E0:.4f} eV")
