from ase.build import bulk
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.velocityverlet import VelocityVerlet
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
atoms.set_calculator(EMT())

initial = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy: {initial:.3f} eV")

dyn = VelocityVerlet(atoms, timestep=1e-3)
dyn.run(50)

final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final total energy: {final:.3f} eV")
