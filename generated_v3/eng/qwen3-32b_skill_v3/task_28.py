from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# MD parameters
t_initial = 300.0
t_final = 600.0
n_steps = 200
dt = 5 * units.fs
friction = 0.01 / units.fs

# Initialize Langevin
md = Langevin(atoms, dt, t_initial, friction)

for step in range(n_steps):
    step_num = step + 1
    current_T = t_initial + (t_final - t_initial) * step_num / n_steps
    md.temperature_K = current_T
    md.run(1)
    if step_num % 50 == 0:
        print(f"Step {step_num}: Temperature = {current_T:.1f} K")
