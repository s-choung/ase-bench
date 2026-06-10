from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

def temp_ramp(step):
    return 300.0 + 300.0 * step / 200.0

dyn = Langevin(atoms, timestep=5.0 * units.fs, temperature=temp_ramp, friction=0.01)

def print_temp():
    step = dyn.get_number_of_steps()
    if step % 50 == 0:
        print(f"Step {step}: T = {atoms.get_temperature():.1f} K")

dyn.attach(print_temp, interval=1)
dyn.run(200)
