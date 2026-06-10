from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.md.thermostat import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 500 * units.kB)
timestep = 5 * units.fs
dyn = VelocityVerlet(atoms, timestep)
bussi = Bussi(atoms, temperature_K=500, timestep=timestep)
dyn.attach(bussi, interval=1)

def print_temp():
    print(f'Temperature: {atoms.get_temperature():.2f} K')

dyn.attach(print_temp, interval=50)
dyn.run(200)
