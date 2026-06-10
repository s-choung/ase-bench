import ase.units as units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import BussiThermostat
from ase.md import VelocityVerlet

# Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09, cubic=True) * (2, 2, 2)
atoms.calc = EMT()
atoms.set_velocities(atoms.get_random_velocities(500))

# NVT with Bussi thermostat
thermostat = BussiThermostat(temperature=500 * units.kB)
dt = 5.0 * units.fs
dyn = VelocityVerlet(atoms, timestep=dt, thermostat=thermostat)

def print_temp():
    print(f"Step {dyn.get_number_of_steps()}: T = {atoms.get_temperature():.2f} K")
dyn.attach(print_temp, interval=50)

dyn.run(200)
