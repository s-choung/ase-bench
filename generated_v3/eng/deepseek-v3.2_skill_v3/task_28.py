from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2,15))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def print_temp(atoms=atoms):
    print(f'Step {dyn.nsteps}: T = {atoms.get_temperature():.1f} K')

dyn = Langevin(atoms, 5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
dyn.attach(print_temp, interval=50)

target_temp = 600
ramp_rate = (target_temp - 300) / 200

def ramp_temperature(dyn=dyn):
    dyn.temperature_K = 300 + ramp_rate * dyn.nsteps

dyn.attach(ramp_temperature, interval=1)
dyn.run(200)
