from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.nosehoover import NoseHooverChain
from ase import units

atoms = bulk('Ag', 'fcc', a=4.08) * (2, 2, 2)
atoms.calc = EMT()
thermostat = NoseHooverChain(atoms, temperature_K=500, chainlength=3)
dyn = VelocityVerlet(atoms, 5 * units.fs)
dync.attach(thermostat.update, interval=1)
def print_temp(step):
    if not step % 50:
        print(f'Step {step}: {atoms.get_temperature():.2f} K')
dync.attach(print_temp, interval=1)
dync.run(200)
