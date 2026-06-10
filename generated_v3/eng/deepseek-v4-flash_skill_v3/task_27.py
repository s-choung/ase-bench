from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Create 2x2x2 supercell of Ag FCC
atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities for NVT at 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Bussi thermostat
dyn = Bussi(atoms, timestep=5 * units.fs, temperature_K=500, taut=100 * units.fs)

# Run 200 steps, print temperature every 50 steps
for step in range(0, 200, 50):
    dyn.run(50)
    T = atoms.get_temperature()
    print(f"Step {step + 50}, Temperature: {T:.2f} K")
