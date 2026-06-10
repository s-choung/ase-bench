from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.md.thermostats import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09, cubic=True) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

thermo = Bussi(atoms, temperature=500, taut=100 * units.fs)

dyn = VelocityVerlet(atoms, dt=5.0 * units.fs)

def print_T():
    print(f'T = {atoms.get_temperature():.2f} K')

dyn.attach(thermo.run, interval=1)
dyn.attach(print_T, interval=50)
dyn.run(200)
