from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.io import read, write
import tempfile
import os

# Create Cu FCC bulk
a = 3.61  # Lattice constant for Cu in Angstroms
cu = Atoms('Cu4', 
           positions=[[0, 0, 0], [0, a/2, a/2], [a/2, 0, a/2], [a/2, a/2, 0]],
           cell=[a, a, a],
           pbc=True)

# Attach EMT calculator
cu.calc = EMT()

# Create temporary trajectory file
temp_fd, temp_path = tempfile.mkstemp(suffix='.traj')
os.close(temp_fd)

# Run MD for 10 steps
dyn = Langevin(cu, timestep=2*0.044, temperature_K=300, friction=0.02)
dyn.run(10)
write(temp_path, cu)

# Read trajectory back
traj = read(temp_path, ':')
print(f"Total frames: {len(traj)}")
print(f"Energy of last frame: {traj[-1].get_potential_energy()} eV")

# Clean up temporary file
os.unlink(temp_path)
