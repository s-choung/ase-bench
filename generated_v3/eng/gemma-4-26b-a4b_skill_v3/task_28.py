import numpy as np
from ase import units
from ase.build import bulk
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Setup Cu supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
atoms.calc = EMT()

# Initial relaxation
BFGS(atoms).run(fmax=0.05)

# MD setup
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Temperature ramp parameters
t_start, t_end = 300, 600
n_steps = 200
dt = 5 * units.fs

def run_ramp(atoms, step):
    # Linear interpolation for temperature
    current_T = t_start + (t_end - t_start) * (step / n_steps)
    # Friction scaled to maintain stability during ramp
    dyn = Langevin(atoms, timestep=dt, temperature_K=current_T, friction=0.01/units.fs)
    dyn.run(1) # Run 1 step to update temperature
    return current_T

# Simulation loop
print(f"{'Step':>10} | {'Temp (K)':>10}")
print("-" * 25)

for i in range(1, n_steps + 1):
    # Calculate target T for this step
    target_T = t_start + (t_end - t_start) * (i / n_steps)
    
    # Instantiate Langevin with target temperature
    dyn = Langevin(atoms, timestep=dt, temperature_K=target_T, friction=0.01/units.fs)
    dyn.run(1)
    
    if i % 50 == 0 or i == 1:
        print(f"{i:10d} | {atoms.get_temperature():10.2f}")
