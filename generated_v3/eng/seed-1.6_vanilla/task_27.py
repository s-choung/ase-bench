from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.thermostats import Bussi
from ase.units import fs

# Ag FCC 2x2x2 supercell
ag = bulk('Ag', 'fcc').repeat((2,2,2))
ag.calc = EMT()
ag.set_velocities_from_temperature(500)

# NVT MD with Bussi thermostat (5 fs timestep)
dyn = VelocityVerlet(ag, 5 * fs)
dyn.attach(Bussi(dyn, 500), interval=1)

# Print temp every 50 steps
def print_temp():
    print(f'Temperature: {ag.get_temperature():.2f} K')
dyn.attach(print_temp, interval=50)

# Run 200 steps
dyn.run(200)
