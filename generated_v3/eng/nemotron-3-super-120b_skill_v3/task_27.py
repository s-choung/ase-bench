from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.bussi import Bussi

# Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities for 500 K and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Bussi thermostat (NVT)
dyn = Bussi(atoms, timestep=5 * units.fs, temperature_K=500)

# Run 200 steps, printing temperature every 50 steps
for i in range(0, 200, 50):
    dyn.run(50)
    T = atoms.get_temperature()
    print(f'Step {i+50}: T = {T:.2f} K')
