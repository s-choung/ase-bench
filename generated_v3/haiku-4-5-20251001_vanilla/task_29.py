from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.npt import NPT
import numpy as np

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.88, cubic=True)
atoms = atoms.repeat((2, 2, 2))

# Set calculator
atoms.calc = EMT()

# Set initial temperature
T = 500  # K
kb = 8.617333262e-5  # eV/K
v = np.sqrt(3 * kb * T / atoms.get_masses().mean())
atoms.set_velocities(np.random.randn(len(atoms), 3) * v)

# Get initial energy
E_initial = atoms.get_total_energy()
KE_initial = atoms.get_kinetic_energy()
PE_initial = E_initial - KE_initial

# Run MD
md = VelocityVerlet(atoms, timestep=2.0, trajectory=None)
for i in range(200):
    md.run(1)

# Get final energy
E_final = atoms.get_total_energy()
KE_final = atoms.get_kinetic_energy()
PE_final = E_final - KE_final

# Print results
print(f"Initial Total Energy: {E_initial:.6f} eV")
print(f"Final Total Energy: {E_final:.6f} eV")
print(f"Energy Difference: {E_final - E_initial:.6f} eV")
print(f"Energy Conservation Error: {abs(E_final - E_initial):.6e} eV")
