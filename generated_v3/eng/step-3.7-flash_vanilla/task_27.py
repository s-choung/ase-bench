from ase.build import fcc
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.md.bussi import BussiThermostat

atoms = fcc('Ag', size=(2, 2, 2))
atoms.calc = EMT()
T, dt = 500, 5
dyn = VelocityVerlet(atoms, dt=dt, initial_velocities={'temperature': T})
dyn.attach(BussiThermostat(atoms, T, dt).step, interval=1)
dyn.attach(lambda: print(f"Step {dyn.nsteps}: T = {atoms.get_temperature():.1f} K"), interval=50)
dyn.run(200)
