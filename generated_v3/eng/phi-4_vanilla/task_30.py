from ase import Atoms
from ase.build import bulk
from ase.md.npt import NPT
from ase.io import Trajectory
from ase.units import fs, kb
import numpy as np

# Create a Cu bulk structure with a 3x3x3 supercell
cu = bulk('Cu', 'fcc', a=3.61)  # Cu lattice parameter in angstrom
supercell = cu.repeat((3, 3, 3))

# Set up the MD simulation
dyn = NPT(supercell, t_start=0 * kb, t_end=300 * kb, tau_p=1000 * fs, tau_t=100 * fs,
          pressure=1 * 1e5, temperature=300, tstep=5 * fs)

# Attach trajectory writer to save the simulation data
dyn.attach(Trajectory('npt-traj.traj', mode='w'))

# Run the simulation
print("Running NPT MD simulation")
dyn.run(200)

# Print initial and final cell volume and pressure
print(f"Initial cell volume: {supercell.volumes[0]:.3f} Å^3")
print(f"Final cell volume: {supercell.volumes[-1]:.3f} Å^3")
print(f"Simulated Pressure: {supercell.get_stress()[:]/1e5[0]:.3f} bar")
