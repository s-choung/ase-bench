from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet
from ase import units
from ase.io import read, write

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.61)
atoms *= (2, 2, 2)  # Make a 64-atom supercell

# Attach EMT calculator
atoms.calc = EMT()

# Set initial velocity distribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Run MD for 10 steps and save trajectory
with open('Cu_md.traj', 'w') as f:
    pass  # Initialize file
md = VelocityVerlet(atoms, timestep=5*units.fs)
md.attach(lambda: write('Cu_md.traj', atoms, format='traj'), interval=1)
md.run(10)

# Read trajectory back
frames = read('Cu_md.traj', index=':')
n_frames = len(frames)
last_energy = frames[-1].get_potential_energy()

print(f"Total frames: {n_frames}")
print(f"Last frame energy: {last_energy} eV")
