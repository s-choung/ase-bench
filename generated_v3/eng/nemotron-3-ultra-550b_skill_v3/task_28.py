from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)

def ramp_and_print():
    step = dyn.get_number_of_steps()
    if step <= 200:
        dyn.temperature_K = 300 + 300 * step / 200
    if step % 50 == 0:
        print(f"Step {step:3d}: T = {atoms.get_temperature():.1f} K")

dyn.attach(ramp_and_print, interval=1)
dyn.run(200)
