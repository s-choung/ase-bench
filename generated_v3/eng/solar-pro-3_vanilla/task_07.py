from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
import sys

# Bulk Cu FCC lattice, one 2x2x2 unit cell, PBC on
cu = Atoms(
    'Cu',  # composition (1 per primitive cell)
    positions=[[ 0.0,  0.0,  0.0],
              [ 0.5,  0.5,  0.5]],
    cell=[2.56, 2.56, 2.56],
    pbc=True
)

# Calibrate kinetic energy to target temperature 300 K
cu.center()
T = 300  # K
f_max = cu.get_free_energy()
cu.set_velocities(free_energy=f_max, temperature=T)

# Set up EMT calculator
cu.set_calculator(EMT())
totalE0 = cu.get_potential_energy() + cu.get_kinetic_energy()
print(f"Initial total energy {totalE0:.6f}")

# NVE dynamics
dyn = VelocityVerlet(cu, dt=1.0)
print("Running NVE MD for 50 steps")
for i in range(50):
    dyn.run(1)

totalE1 = cu.get_potential_energy() + cu.get_kinetic_energy()
print(f"Final total energy {totalE1:.6f}")

# Check conservation
dE = totalE1 - totalE0
print(f"Energy drift over 50 steps: {dE:.6e}")
if abs(dE) < 1e-6:
    sys.stdout.write("Energy conserved (good)\n")
else:
    sys.stdout.write("Warning: energy drift\n")
