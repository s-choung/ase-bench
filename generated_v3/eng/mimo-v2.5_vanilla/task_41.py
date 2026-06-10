from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.langevin import Langevin
from ase import units
from ase.io import read
import os

# Create Cu FCC bulk
atoms = bulk('Cu', fcc cubic=True)
atoms.cell *= 1.0  # No resizing needed

# Attach EMT calculator
atoms.calc = EMT()

# Set initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# MD with Langevin thermostat
dyn = Langevin(atoms, 
               timestep=5 * units.fs,
               temperature_K=300,
               friction=0.002)

# Run MD and write to trajectory
traj_file = 'cu_md.traj'
dyn.attach(atoms.write, interval=1, filename=traj_file)
dyn.run(steps=10)

# Read trajectory back
frames = read(traj_file, index=':')
n_frames = len(frames)

# Get energy of last frame
energy = frames[-1].get_potential_energy()

print(f"Number of frames: {n_frames}")
print(f"Energy of last frame: {energy:.6f} eV")

# Cleanup
os.remove(traj_file)
