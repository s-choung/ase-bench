import ase.units as units
from ase import Atoms
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

atoms = Atoms('Cu', positions=[[0, 0, 0]], cell=2.55 * units.Bohr, pbc=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

def temperature_ramp(dynamics):
    current_step = dynamics.get_number_of_steps()
    fraction = current_step / 200
    target_temp = 300 + fraction * 300
    dynamics.set_temperature(target_temp * units.kB)

dynamics = Langevin(atoms, 5 * units.fs, 300 * units.kB, 0.002)
dynamics.attach(temperature_ramp, interval=1)
dynamics.attach(lambda: print(f'Step {dynamics.get_number_of_steps()}: T = {dynamics.get_temperature() / units.kB:.1f} K'), interval=50)

dynamics.run(200)
