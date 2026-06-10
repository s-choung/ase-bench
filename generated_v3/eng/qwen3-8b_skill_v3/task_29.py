from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Pd', 'fcc', a=3.8, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
dyn = VelocityVerlet(atoms, dt=2*units.fs)
dyn.run(200)

initial = atoms.get_potential_energy() + atoms.get_kinetic_energy()
final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Energy difference: {final - initial} eV")
