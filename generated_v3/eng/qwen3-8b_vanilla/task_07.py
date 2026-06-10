import ase
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
atoms.set_calculator(EMT())

dyn = VelocityVerlet(atoms, dt=1.0)
dyn.set_temperature(300)
dyn.run(50)

initial_total = atoms.get_potential_energy() + dyn.get_kinetic_energy()
final_total = atoms.get_potential_energy() + dyn.get_kinetic_energy()

print(f"Initial total energy: {initial_total}")
print(f"Final total energy: {final_total}")
