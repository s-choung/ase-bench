from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.units import fs
import numpy as np

# Create Cu FCC bulk
a = 3.6  # lattice constant in Angstrom
cu = Atoms('Cu', positions=[[0, 0, 0]], cell=[a, a, a], pbc=True)
cu *= (2, 2, 2)  # 8-atom supercell

# Set EMT calculator
cu.calc = EMT()

# Set initial velocities for 300 K
 MaxwellBoltzmannDistribution(cu, temperature_K=300)
 Stationary(cu)  # Remove center-of-mass motion
 ZeroRotation(cu)  # Remove rotational motion

# Initial energy
initial_pe = cu.get_potential_energy()
initial_ke = cu.get_kinetic_energy()
initial_total = initial_pe + initial_ke

# Run NVE MD for 50 steps (1 fs timestep)
dyn = VelocityVerlet(cu, 1 * fs)
for _ in range(50):
    dyn.run(1)

# Final energy
final_pe = cu.get_potential_energy()
final_ke = cu.get_kinetic_energy()
final_total = final_pe + final_ke

# Print energies
print(f"Initial total energy: {initial_total:.6f} eV")
print(f"Final total energy:   {final_total:.6f} eV")
