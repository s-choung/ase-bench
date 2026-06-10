from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, 5 * units.fs, temperature_K=300, friction=0.01 / units.fs)

def ramp_and_print():
    step = dyn.nsteps
    T_target = 300 + (600 - 300) * step / 200
    dyn.temp = T_target * units.kB
    if step % 50 == 0:
        print(f"Step {step}: T = {atoms.get_temperature():.2f} K")

dyn.attach(ramp_and_print, interval=1)
ramp_and_print()
dyn.run(200)
