from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# Create 2x2x2 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities at 300K
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Set up Langevin dynamics
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)

# Temperature ramp function
def temperature_ramp(step):
    return 300 + (600 - 300) * (step / 199)  # Linear ramp over 200 steps

# Run MD with temperature ramp
for step in range(200):
    # Update temperature
    current_temp = temperature_ramp(step)
    dyn.temperature_K = current_temp
    dyn.run(1)
    
    # Print temperature every 50 steps
    if step % 50 == 0:
        print(f"Step {step}: Target T = {current_temp:.1f}K, Actual T = {atoms.get_temperature():.1f}K")

print(f"Final step: Target T = {temperature_ramp(199):.1f}K, Actual T = {atoms.get_temperature():.1f}K")
