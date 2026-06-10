from ase.build import fcc111
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT

atoms = fcc111('Cu', size=(2, 2, 2), vacuum=1.0)

calc = EMT()
atoms.set_calculator(calc)

dyn = Langevin(atoms, 300.0, 5.0, 0.02)

def print_state(a, state):
    print(f"Step {state.step}: Temperature = {a.get_temperature():.2f} K, Energy = {a.get_potential_energy():.5f} eV")

print_state(atoms, dyn.get_state())

for step in range(100):
    dyn.run(1)
    
print_state(atoms, dyn.get_state())
