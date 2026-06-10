from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Create Cu FCC 2x2x2 supercell (conventional cell repeated)
atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)
atoms.set_calculator(EMT())

# Set initial velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Langevin thermostat with initial temperature 300 K, friction 0.01 fs^-1
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01)

# Ramp from 300 K to 600 K over 200 steps
for step in range(200):
    T = 300 + step * 1.5  # linear ramp
    dyn.temperature = T
    dyn.run(1)
    if (step + 1) % 50 == 0:
        print(f"Step {step+1}, Temperature: {dyn.temperature:.1f} K")
