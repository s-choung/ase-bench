from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# Create Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2,2,2))
atoms.calc = EMT()

# Initialize velocities at 300K
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Set up Langevin dynamics
dyn = Langevin(atoms, timestep=5.0*units.fs, temperature_K=300, friction=0.01)

# Temperature ramp function
def ramp_temperature(step):
    if step < 200:
        return 300 + (600-300) * (step/199)
    return 600

# MD loop
for step in range(200):
    # Update temperature
    current_temp = ramp_temperature(step)
    dyn.set_temperature(temperature_K=current_temp)
    
    # Take integration step
    dyn.run(1)
    
    # Print temperature every 50 steps
    if step % 50 == 0:
        inst_temp = atoms.get_temperature()
        print(f"Step {step}: Set Temp = {current_temp:.1f} K, Inst. Temp = {inst_temp:.1f} K")
