from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet, Bussi
from ase import units
from ase.md.maxwellboltzmann import MaxwellBoltzmannDistribution

# Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities for 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500.0)

timestep = 5 * units.fs
dyn = VelocityVerlet(atoms, timestep)

# Bussi thermostat (stochastic velocity rescaling)
dyn.attach(Bussi(atoms, temperature_K=500.0, tau=100 * units.fs), interval=1)

def print_temperature():
    step = dyn.nsteps
    T = atoms.get_temperature()
    print(f'{step} {T:.2f}')

dyn.attach(print_temperature, interval=50)

dyn.run(200)
