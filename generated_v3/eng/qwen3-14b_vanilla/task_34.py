import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

# Create FCC(111) slab
slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)

# Identify top layer atoms
positions = slab.get_positions()
z = positions[:, 2]
top_layer_indices = np.where(z == np.max(z))[0]
top_layer = slab[top_layer_indices[:3]]  # First three atoms in top layer

# Calculate average position for FCC hollow site and adjust z
fcc_pos = np.mean(top_layer.get_positions(), axis=0)
fcc_pos[2] += 2.0  # Adjust z-coordinate for adatom

# Create initial configuration with adatom at FCC site
initial = slab.copy()
initial.append(ase.Atom('Cu', position=fcc_pos))

# Create final configuration with adatom at HCP site (roughly shifted)
hcp_pos = fcc_pos + np.array([1.5, 0, 0])
final = slab.copy()
final.append(ase.Atom('Cu', position=hcp_pos))

# Prepare images for NEB
images = [initial.copy(), final.copy()]
neb = NEB(images, method='idpp')
neb.interpolate(nimages=5)

# Set calculator
for img in images:
    img.set_calculator(EMT())

# Optimize using BFGS
opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

# Calculate energy barrier
energies = [img.get_potential_energy() for img in images]
initial_energy = energies[0]
max_energy = max(energies)
barrier = max_energy - initial_energy
print(f"Energy barrier: {barrier:.3f} eV")
