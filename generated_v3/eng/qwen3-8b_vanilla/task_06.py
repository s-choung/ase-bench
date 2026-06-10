import ase
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import Langevin

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)
atoms.set_calculator(EMT())

initial_energy = atoms.get_potential_energy()
initial_temp = 300

dyn = Langevin(atoms, timestep=5.0, temperature_K=300, friction=0.01)
dyn.run(100)

final_energy = atoms.get_potential_energy()
final_temp = atoms.get_temperature()

print(f"Initial Temp: {initial_temp} K")
print(f"Final Temp: {final_temp} K")
print(f"Initial Energy: {initial_energy} eV")
print(f"Final Energy: {final_energy} eV")
