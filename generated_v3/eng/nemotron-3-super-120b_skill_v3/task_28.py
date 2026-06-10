from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc')  # uses ASE's default lattice constant
atoms = atoms * (2, 2, 2)   # 2x2x2 supercell

# Attach calculator
atoms.calc = EMT()

# Initialize velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Set up Langevin dynamics (initial temperature 300 K)
dyn = Langevin(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    friction=0.01 / units.fs,
)

# Temperature ramp parameters
T_start = 300.0
T_end = 600.0
n_steps = 200
delta_T = (T_end - T_start) / n_steps

# Run MD with temperature ramp
for step in range(n_steps):
    dyn.step()
    # Update target temperature for next step
    dyn.temperature_K = T_start + delta_T * (step + 1)
    # Print every 50 steps
    if (step + 1) % 50 == 0:
        current_T = atoms.get_temperature()
        print(f"Step {step+1}: T = {current_T:.2f} K")

# Final temperature
print(f"Final step {n_steps}: T = {atoms.get_temperature():.2f} K")
