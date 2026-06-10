from ase.build import fcc111, add_adatom
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
import numpy as np

# Build a Cu(111) surface
slab = fcc111('Cu', size=(3, 3, 4))

# Add a Cu adatom to a hollow site
add_adatom(slab, 'Cu', site='fcc')

# Define the initial and final configurations
initial = slab.copy()
final = slab.copy()

# Move the adatom to an HCP hollow site
indices = np.where(slab.get_scaled_positions()[:, 2] == 3.68)[0]
final.get_positions()[indices[0]] = [1.5, 1.5, 3.68]

# Create the NEB
neb = NEB(initial, final, nsteps=100)
neb.skin = 3.0

# Set the calculator
neb.calc = EMT()

# Optimize the path
neb.run(fmax=0.02)

# Calculate the energy barrier
energy_barrier = neb.energy[0] - neb.energy[-1]

# Print the energy barrier
print(f"Energy barrier: {energy_barrier:.3f} eV")
