from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.velocitydistribution import BoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Pd', 'fcc', cubic=True).repeat((2,2,2))
atoms.set_calculator(EMT())
BoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
E_initial = atoms.get_kinetic_energy() + atoms.get_potential_energy()
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)
E_final = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Energy difference: {E_final - E_initial:.4f} eV")
