from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Create 2x2x2 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.615).repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities at 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Set up Langevin thermostat
langevin = Langevin(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    friction=0.01 / units.fs
)

# Run 200 steps with temperature ramp from 300K to 600K
for step in range(200):
    # Linear temperature ramp
    current_target_T = 300 + 300 * (step / 199)
    langevin.temperature_K = current_target_T
    # Run 1 MD step
    langevin.run(1)
    # Print temperature every 50 steps
    if (step + 1) % 50 == 0:
        actual_temp = atoms.get_temperature()
        print(f"Step {step+1:3d}: Actual T = {actual_temp:.1f} K, Target T = {current_target_T:.1f} K")
