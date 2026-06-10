from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, StochasticVelocityRescaling
from ase.md import VelocityVerlet

atoms = bulk('Ag', 'fcc') * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 500.0)
thermostat = StochasticVelocityRescaling(atoms, 500, 100 * units.fs)
dyn = VelocityVerlet(atoms, 5 * units.fs)

print(f"Step {0}: T = {atoms.get_temperature():.2f} K")
dyn.attach(thermostat, interval=1)
dyn.attach(lambda dyn: print(f"Step {dyn.nsteps}: T = {dyn.atoms.get_temperature():.2f} K"), interval=50)
dyn.run(200)
