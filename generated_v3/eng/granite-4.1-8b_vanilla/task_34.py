from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import fcc111, add_adsorbate
from ase.neb import NEB
from ase.optimize import BFGS
from ase.io import read, write
from ase.constraints import FixAtoms
import numpy as np

# Create Cu(111) surface
surface = fcc111('Cu', size=(3, 3, 4))
surface.center(vacuum=10)

# Define adatom positions for fcc and hcp sites
fcc_hollow = [0.25, 0.25, 0.515]
hcp_hollow = [0.125, 0.375, 0.515]

# Add Cu adatom to the surface
adatom_fcc = add_adsorbate(surface, 'Cu', fcc_hollow, 2.0)
adatom_hcp = add_adsorbate(surface, 'Cu', hcp_hollow, 2.0)

# Create images for NEB
images = [adatom_fcc] + [Atoms(cell=surface.cell) for _ in range(3)] + [adatom_hcp]

# Set constraints to keep surface atoms fixed
mask = [i for i, a in enumerate(images[0]) if a.symbol != 'Cu']
for img in images:
    img.set_constraint(FixAtoms(mask=[not i for i in mask]))

# Attach EMT calculator
cal = EMT()
for img in images:
    img.set_calculator(cal)

# Initialize NEB with 5 images (including end points)
band = NEB(images, interpolate=5)
band.interpolate()

# Optimize the NEB images
opt = BFGS(band, qenthalpy=False)
opt.run(fmax=0.05)

# Calculate energies
energies = [img.get_potential_energy() for img in band.images]

# Energy barrier calculation
initial_energy = energies[0]
max_energy = max(energies)
energy_barrier = max_energy - initial_energy

print(f"Energy barrier: {energy_barrier:.3f} eV")

# Optionally write the final path to a file
write('diffusion_path.traj', band.images)
