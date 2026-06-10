from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities for 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Bussi thermostat, 5 fs timestep
dyn = Bussi(atoms,
            timestep=5 * units.fs,
            temperature_K=500,
            ttime=50 * units.fs)

# Callback to print temperature every 50 steps
def print_temp():
    print(f"Step {dyn.nsteps}: T = {atoms.get_temperature():.2f} K")

dyn.attach(print_temp, interval=50)

# Run 200 steps
dyn.run(200)
