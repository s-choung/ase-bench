from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
atoms.calc = EMT()

def temp_func(t):
    return 300 + 300 * t / 1000.0

dyn = Langevin(atoms, 5*units.fs, temperature_K=temp_func, friction=0.01)

def print_temp():
    step = dyn.get_number_of_steps()
    t = dyn.get_time()
    print(f"Step {step}: Temperature = {temp_func(t):.1f} K")

dyn.attach(print_temp, interval=50, first=0)
dyn.run(200)
