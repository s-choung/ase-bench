from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import fs

def temp_ramp(step):
    return 300 + 300 * (step / 199)

def print_callback(dyn):
    step = dyn.get_number_of_steps()
    steps_done = step + 1
    if steps_done % 50 == 0:
        print(f'Steps: {steps_done}, Temp: {dyn.atoms.get_temperature():.2f} K')

atoms = bulk('Cu', 'fcc').repeat((2,2,2))
atoms.calc = EMT()

dyn = Langevin(atoms, timestep=5*fs, temperature=temp_ramp, friction=0.01)
dyn.attach(print_callback, interval=1)
dyn.run(200)
