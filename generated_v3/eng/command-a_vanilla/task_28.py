from ase import Atoms
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase.lattice.cubic import FaceCenteredCubic
import numpy as np

# Create Cu FCC 2x2x2 supercell
cu = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                       size=(2, 2, 2), symbol='Cu', pbc=True)
cu.calc = EMT()

# Initial and final temperatures
T_initial = 300
T_final = 600
steps = 200
timestep = 5e-3  # fs
friction = 0.01

# Temperature ramp parameters
delta_T = (T_final - T_initial) / steps

# Langevin dynamics
dyn = Langevin(cu, timestep * 0.001, T_initial, friction, trajectory=None)

# Run dynamics with temperature ramp
for step in range(steps):
    T_current = T_initial + step * delta_T
    dyn.set_temperature(T_current)
    dyn.run(1)
    if (step + 1) % 50 == 0:
        print(f"Step {step + 1}: Temperature = {cu.get_kinetic_energy() / (1.5 * len(cu)) * (len(cu) / 3.1668295465585):.2f} K")
