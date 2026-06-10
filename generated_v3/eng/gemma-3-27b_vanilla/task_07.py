from ase.build import fcc111
from ase.md.velocityverlet import VelocityVerlet
from ase.calculators.emt import EMT

atoms = fcc111('Cu', size=(3, 3, 3), vacuum=1.0)
calc = EMT()
atoms.set_calculator(calc)

temps = 300
VelocityVerlet(atoms, 0.01, trajectory='Cu_MD.traj').run(50, thermostat=temps)

initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {initial_energy} eV")
print(f"Final total energy: {final_energy} eV")
