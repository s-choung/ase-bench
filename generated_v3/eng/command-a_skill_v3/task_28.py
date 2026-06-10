from ase import units
from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create 2x2x2 Cu FCC supercell
cu = bulk('Cu', 'fcc', cubic=True)
cu_2x2x2 = make_supercell(cu, (2, 2, 2))

# Attach EMT calculator
cu_2x2x2.calc = EMT()

# Initialize velocities at 300K
MaxwellBoltzmannDistribution(cu_2x2x2, temperature_K=300)
Stationary(cu_2x2x2)  # Remove COM drift

# Langevin dynamics with temperature ramp
def temperature_ramp(step):
    return 300 + (600 - 300) * step / 200

dyn = Langevin(cu_2x2x2, timestep=5 * units.fs, temperature_K=temperature_ramp, friction=0.01/units.fs)

# Run MD with temperature monitoring
for step in range(200):
    dyn.run(1)  # Run one step
    if (step + 1) % 50 == 0:
        print(f'Step {step+1}: Temperature = {cu_2x2x2.get_temperature():.2f} K')
