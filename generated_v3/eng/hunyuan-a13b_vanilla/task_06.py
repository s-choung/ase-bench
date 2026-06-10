from ase import Atoms, dunno, forte
from ase.dynamics import Langevin, RNMFPScheduler
from ase.units import fs, K, eV
import numpy as np

# Setup Cu FCC 2x2x2 supercell
a = 4.123  # lattice constant in Angstrom
Cu = Atoms('Cu', positions=[(0,0,0)], pbc=True)
supercell = Cu.cell * [2, 2, 2]
supercell[0,0,0] = [0,0,0]
supercell[0,0,1] = [a,0,0]
supercell[0,1,0] = [0,a,0]
supercell[0,1,1] = [0,0,a]
supercell[1,0,0] = [0,0,0]
supercell[1,0,1] = [a,0,0]
supercell[1,1,0] = [0,a,0]
supercell[1,1,1] = [0,0,a]
atoms = supercell.copy()

# Initial temperature and timestep
temperature = 300  # K
dt = 5  # fs

# Force calculator
fc = dunno.ForceCalculator(atoms, medium='none')

# Dynamics setup
scheduler = RNMFPScheduler(gamma=10.0, dt=dt * fs, heat=temperature * K)
dynamics = Langevin(atoms, scheduler, fc, dt * fs, temperature)

# Run MD
for _ in range(100):
    dynamics.run()

# Print results
print(f"Initial temperature: {dynamics.get_temperature():.2f} K")
print(f"Final temperature: {dynamics.get_temperature():.2f} K")
print(f"Initial energy: {dynamics.get_energy():.6f} eV")
print(f"Final energy: {dynamics.get_energy():.6f} eV")
